import time
import numpy as np
from hmsolver.meshgrid import Zone2d
from hmsolver.femcore import read_mesh_to_MeshObject
from hmsolver.meshgrid import HybridCrackMesh2d
from hmsolver.material import PdMaterial2d
from hmsolver.femcore import point_criteria, segment_criteria
from hmsolver.femcore import boundary_cond2d, BoundaryConds2d
from hmsolver.app import CrackSimulation2d
from hmsolver.basis import Quad4Node
from hmsolver.utils import formatting_time

import sys
import argparse
import pickle

def main(example_name, mesh_file_name, cname, total_phase=5):
    t0 = time.time()  # tic
    # 几何区域
    zone_xl, zone_xr = 0, 1
    zone_yl, zone_yr = 0, 1
    zone_xmid = 0.5 * (zone_xl + zone_xr)
    zone_ymid = 0.5 * (zone_yl + zone_yr)
    inner_hole_radius = 0.1
    notch_width, notch_depth = 0.05, 0.4
    notch_height = 0.25
    total_area = (zone_yr - zone_yl) * (zone_xr - zone_xl)
    total_area -= np.pi * (inner_hole_radius**2)
    total_area -= notch_width * notch_depth + 0.5 * np.pi * (notch_width/2)**2
    zone = Zone2d(zone_xl, zone_xr, zone_yl, zone_yr)

    # 加载网格剖分结果
    mesh2d = read_mesh_to_MeshObject(mesh_file_name, HybridCrackMesh2d)
    n_nodes, n_elements = mesh2d.n_nodes, mesh2d.n_elements

    # 新增预制裂纹（边界裂纹）
    notch_points = [(zone_xl, zone_yl + notch_height),
    (zone_xl + notch_depth, zone_yl + notch_height),
    (zone_xl + notch_depth + 0.5 * notch_width, zone_yl + notch_height + 0.5 * notch_width),
    (zone_xl + notch_depth, zone_yl + notch_height + notch_width),
    (zone_xl, zone_yl + notch_height + notch_width)]
    mesh2d.initCracks([(pA, pB) for pA, pB in zip(notch_points[:4], notch_points[1:])])

    # 计算平均网格大小
    grid_size = np.sqrt(total_area / n_elements)

    # 输出网格基本信息
    print(f"Mesh contains {n_nodes} nodes and {n_elements} elements.")
    print(f"Average Grid Size= {grid_size:.8f}")

    # 建立材料实例
    if cname == "constant":
        material2d = PdMaterial2d(192e9, 1.0 / 3)
    elif cname == "attenuate":
        material2d = PdMaterial2d(192e9, 1.0 / 3, attenuation_term_config="exp")

    # 边界条件
    shear = 0.04
    boundary_1 = segment_criteria(zone_xl, zone_yl, zone_xr, zone_yl)
    boundary_2 = segment_criteria(zone_xl, zone_yr, zone_xr, zone_yr)
    boundary_3 = segment_criteria(zone_xl, zone_yr, zone_xmid, zone_yr)
    _bc_ = boundary_cond2d  # abbreviate the word for type & read
    boundarys = BoundaryConds2d(
        _bc_("segment", boundary_1, "set_ux", "constant", +shear),
        _bc_("segment", boundary_1, "set_uy", "constant", 0),
        _bc_("segment", boundary_2, "fixed", None, None))
    del _bc_  # delete the abbreviation
    boundarys.manually_verify()

    # 建立断裂模拟实例
    app = CrackSimulation2d(mesh2d, material2d, boundarys)
    app.app_name = example_name
    app.parallelized = True # 开启并行多线程
    app.material.stretch_crit = 0.02
    horizon_radius = grid_size * 3
    inst_len = grid_size / 3.0
    app.material.setPeridynamic(horizon_radius, grid_size, inst_len)
    app.mesh.peridynamic_construct(horizon_radius, 2 * horizon_radius,
                                   4 * horizon_radius)
    app.apply_basis(Quad4Node())
    app.check_engine()

    # 自适应添加损伤点
    app.export_to_tecplot("hybrid-start", *app.provied_solutions)
    app.manual_set_gaint_unbroken_zone(boundary_1)
    app.manual_set_gaint_unbroken_zone(boundary_3)
    app.using_peridynamics_only()

    # 运行断裂模拟
    app.run_simulation(total_phase)
    app.export_to_tecplot("hybrid", *app.provied_solutions)
    print(f"Total time cost: {formatting_time(time.time() - t0)}") # toc


if __name__ == '__main__':
    # 基础配置
    # name := "C"       # 算例名
    # runid             # 子算例名 options: 1
    # meshtype          # 网格名 options: 1, 2
    # constitutive      # 本构模型 options: "const", "exp"
    # phase             # 拟静态断裂加载步数 options: $\mathbb Z^+$ positive intergers
    arg = argparse.ArgumentParser(f"python {sys.argv[0]}")
    arg.add_argument("-n", "--name", metavar="str", default="C", type=str, help="name of simulation")
    arg.add_argument("-r", "--runid", metavar="int", default=1, type=int, help="sub number(runid) of simulation")
    arg.add_argument("-t", "--mtype", metavar="int", default=1, type=int, help="mesh type of simulation")
    arg.add_argument("-c", "--ctype", metavar="str", default="const", type=str, help="constitutive type")
    arg.add_argument("-p", "--phase", metavar="int", default=5, type=int, help="total phase of simulation")
    args = arg.parse_args()
    constitutive_mapping = {"const":("A", "constant"), "exp": ("B", "attenuate")}
    c, cname = constitutive_mapping[args.ctype]
    example_name = f"example-{args.name}{args.runid}{c}-{cname}"
    mesh_file_name = f"B{args.runid}{args.mtype}.mesh"
    main(example_name, mesh_file_name, cname, args.phase)
