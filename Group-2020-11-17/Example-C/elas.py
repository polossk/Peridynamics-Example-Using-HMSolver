import time
import numpy as np
from hmsolver.meshgrid import Zone2d
from hmsolver.femcore import read_mesh_to_MeshObject
from hmsolver.meshgrid import HybridMesh2d
from hmsolver.material import PdMaterial2d
from hmsolver.femcore import point_criteria, segment_criteria
from hmsolver.femcore import boundary_cond2d, BoundaryConds2d
from hmsolver.app import Simulation2d
from hmsolver.basis import Quad4Node
from hmsolver.utils import formatting_time

if __name__ == '__main__':
    # tic
    t0 = time.time()

    # 基础配置
    name = "C" # 算例名
    run_id = 1 # 子算例名
    mesh_type = "2" # 网格名 options: "1", "2"

    # 几何区域
    zone_xl, zone_xr = 0, 1
    zone_yl, zone_yr = 0, 1
    zone_xmid = 0.5 * (zone_xl + zone_xr)
    zone_ymid = 0.5 * (zone_yl + zone_yr)
    inner_hole_radius = 0.2
    notch_width, notch_depth = 0.1, 0.4
    total_area = (zone_yr - zone_yl) * (zone_xr - zone_xl)
    total_area -= np.pi * (inner_hole_radius**2)
    total_area -= notch_width * notch_depth + 0.5 * np.pi * (notch_width/2)**2
    zone = Zone2d(zone_xl, zone_xr, zone_yl, zone_yr)

    # 加载网格剖分结果
    mesh_file_name = f"{name}{run_id}{mesh_type}.mesh"
    mesh2d = read_mesh_to_MeshObject(mesh_file_name, HybridMesh2d)
    n_nodes, n_elements = mesh2d.n_nodes, mesh2d.n_elements

    # 计算平均网格大小
    grid_size = np.sqrt(total_area / n_elements)

    # 输出网格基本信息
    print(f"Mesh contains {n_nodes} nodes and {n_elements} elements.")
    print(f"Average Grid Size= {grid_size:.8f}")

    # 建立材料实例
    material2d = PdMaterial2d(192e9, 1.0 / 3)

    # 边界条件
    shear = 0.04
    boundary_1 = segment_criteria(zone_xl, zone_yl, zone_xr, zone_yl)
    boundary_2 = segment_criteria(zone_xl, zone_yr, zone_xr, zone_yr)
    _bc_ = boundary_cond2d  # abbreviate the word for type & read
    boundarys = BoundaryConds2d(
        _bc_("segment", boundary_1, "set_ux", "constant", +shear),
        _bc_("segment", boundary_1, "set_uy", "constant", 0),
        _bc_("segment", boundary_2, "fixed", None, None))
    del _bc_  # delete the abbreviation
    boundarys.manually_verify()

    # 建立模拟实例
    app = Simulation2d(mesh2d, material2d, boundarys)
    app.app_name = f"{name}{run_id}{mesh_type}"
    app.parallelized = True # 开启并行多线程
    app.apply_basis(Quad4Node())
    app.check_engine()

    # 输出模拟结果
    app.export_to_tecplot(f"elasticity", *app.provied_solutions)
    print(f"Total time cost: {formatting_time(time.time() - t0)}")
