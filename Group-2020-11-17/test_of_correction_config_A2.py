import numpy as np
import time
import sys
import argparse
import pickle

import hmsolver.geometry as geometry
from hmsolver.app import Simulation2d
from hmsolver.app import PdSimulation2d
from hmsolver.basis import Quad4Node
from hmsolver.meshgrid import Zone2d, HybridMesh2d
from hmsolver.material import PdMaterial2d
from hmsolver.femcore import point_criteria
from hmsolver.femcore import segment_criteria
from hmsolver.femcore import rectangle_criteria
from hmsolver.femcore import boundary_cond2d as _bc_  # abbreviate the word for type & read
from hmsolver.femcore import BoundaryConds2d
from hmsolver.femcore import read_mesh_to_MeshObject
from hmsolver.utils import formatting_time


def mse(sth):
    return np.sqrt(np.dot(sth, sth) / max(sth.shape))


def mae(sth):
    return np.max(np.abs(sth))


def mse2l2e(sth, N, h):
    return np.sqrt(sth**2 * h**2 * N)


def output_error(u_err_0, u_err_1, runid, grid_size, export_filename):
    n_nodes = u_err_0.shape[0]
    # mean square error
    mse_ux_0, mse_uy_0, mse_ux_1, mse_uy_1 = [
        mse2l2e(mse(_), n_nodes, grid_size)
        for _ in [u_err_0[:, 0], u_err_0[:, 1], u_err_1[:, 0], u_err_1[:, 1]]
    ]
    # maximum absolute error
    mae_ux_0, mae_uy_0, mae_ux_1, mae_uy_1 = [
        mae(_)
        for _ in [u_err_0[:, 0], u_err_0[:, 1], u_err_1[:, 0], u_err_1[:, 1]]
    ]
    # output to file
    with open(export_filename, "a", encoding='utf-8') as fout:
        print("\n## Runid", runid, file=fout)
        print("grid_size=", grid_size, file=fout)
        print("before: mse_ux =", mse_ux_0, file=fout)
        print("before: mse_uy =", mse_uy_0, file=fout)
        print("after:  mse_ux =", mse_ux_1, file=fout)
        print("after:  mse_uy =", mse_uy_1, file=fout)
        print("before: mae_ux =", mae_ux_0, file=fout)
        print("before: mae_uy =", mae_uy_0, file=fout)
        print("after:  mae_ux =", mae_ux_1, file=fout)
        print("after:  mae_uy =", mae_uy_1, file=fout)


def output_kavg(kavg_old, kavg_new, export_filename):
    kavg_new = np.array(kavg_new)
    kavg_old = np.array(kavg_old)
    difference = kavg_new - kavg_old
    err_L2 = mse(difference)
    err_Linf = mae(difference)
    err_relative = np.max(np.abs(difference) / (kavg_new + 1e-8))
    # output to file
    with open(export_filename, "a", encoding='utf-8') as fout:
        print("kavg error(L2)   :=", err_L2, file=fout)
        print("kavg error(Linf) :=", err_Linf, file=fout)
        print("relative error   :=", f"{err_relative * 100:.5f}%", file=fout)


def main(example_name, mesh_config, cname, export_filename):
    t0 = time.time()
    zone_xl, zone_xr = 0, 1
    zone_yl, zone_yr = 0, 2
    zone_xmid = 0.5 * (zone_xl + zone_xr)
    zone_ymid = 0.5 * (zone_yl + zone_yr)
    inner_hole_radius = 0.1
    total_area = (zone_yr - zone_yl) * (zone_xr - zone_xl)
    total_area -= np.pi * (inner_hole_radius**2)
    zone = Zone2d(zone_xl, zone_xr, zone_yl, zone_yr)
    # 网格配置
    mesh2d = read_mesh_to_MeshObject(mesh_file_name, HybridMesh2d)
    n_nodes, n_elements = mesh2d.n_nodes, mesh2d.n_elements
    grid_size = np.sqrt(total_area / n_elements)
    print(f"Mesh contains {n_nodes} nodes and {n_elements} elements.")
    print(f"Average Grid Size= {grid_size:.8f}")
    ratio = 3  # 近场邻域比例
    horizon_radius, inst_len = ratio * grid_size, grid_size / 3.0
    if cname == "constant":
        material2d = PdMaterial2d(192, 1.0 / 3)
    elif cname == "attenuate":
        material2d = PdMaterial2d(192, 1.0 / 3, attenuation="exp")
        # material2d = PdMaterial2d(192, 1.0 / 3, attenuation="exp", is_simplest=True)

    # yapf: disable
    stretch = 0.1
    center_yl = point_criteria(zone_xmid, zone_yl)
    center_yr = point_criteria(zone_xmid, zone_yr)
    dirichlet_yl = segment_criteria(zone_xl, zone_yl, zone_xr, zone_yl)
    dirichlet_yr = segment_criteria(zone_xl, zone_yr, zone_xr, zone_yr)
    cline_xmid = segment_criteria(zone_xmid, zone_yl, zone_xmid, zone_yr)
    cline_ymid = segment_criteria(zone_xl, zone_ymid, zone_xr, zone_ymid)

    boundarys_ccm = BoundaryConds2d()
    boundarys_ccm.append(_bc_("point", center_yl, "set_ux", "constant", 0))
    boundarys_ccm.append(_bc_("point", center_yr, "set_ux", "constant", 0))
    boundarys_ccm.append(_bc_("segment", dirichlet_yl, "set_uy", "constant", 0))
    boundarys_ccm.append(_bc_("segment", dirichlet_yr, "set_uy", "constant", +stretch))
    boundarys_ccm.manually_verify()
    # yapf: enable

    app_ccm = Simulation2d(mesh2d, material2d, boundarys_ccm)
    app_ccm.parallelized = True
    app_ccm.app_name = example_name
    app_ccm.apply_basis(Quad4Node())
    app_ccm.check_engine()
    app_ccm.export_to_tecplot("elasticity", *app_ccm.provied_solutions)

    # yapf: disable
    # uncomment these lines only if you want to constrain a boundary layer
    thickness = ratio * grid_size
    pd_dirichlet_yl = rectangle_criteria(zone_xl, zone_yl, zone_xr, zone_yl + thickness)
    pd_dirichlet_yr = rectangle_criteria(zone_xl, zone_yr - thickness, zone_xr, zone_yr)
    # uncomment end

    # apply boundary conditions to PD problem
    boundarys_pd = BoundaryConds2d()
    boundarys_pd.append(_bc_("segment", cline_xmid, "set_ux", "constant", 0))
    boundarys_pd.append(_bc_("segment", cline_ymid, "set_uy", "constant", 0.5 * +stretch))
    # boundarys_pd.append(_bc_("segment", dirichlet_yl, "set_uy", "constant", 0))
    # boundarys_pd.append(_bc_("segment", dirichlet_yr, "set_uy", "constant", +stretch))
    # uncomment these lines only if you want to constrain a boundary layer
    boundarys_pd.append(_bc_("group", pd_dirichlet_yl, "set_ux_uy", "dictionary", app_ccm.u))
    boundarys_pd.append(_bc_("group", pd_dirichlet_yr, "set_ux_uy", "dictionary", app_ccm.u))
    # uncomment end
    boundarys_pd.manually_verify()
    # yapf: enable

    app_pd = PdSimulation2d(mesh2d, material2d, boundarys_pd)
    # app_pd.parallelized = True
    app_pd.app_name = example_name
    app_pd.material.setPeridynamic(horizon_radius, grid_size, inst_len)
    app_pd.mesh.peridynamic_construct(horizon_radius, 2 * horizon_radius,
                                      4 * horizon_radius)
    app_pd.apply_basis(Quad4Node())
    app_pd.check_engine()
    app_pd.export_to_tecplot("peridynamic-without-correction",
                             *app_pd.provied_solutions)
    wpd_0 = app_pd.get_pd_elastic_energy_density()
    app_pd.export_custom_data_to_tecplot("peridynamic-energy-density",
                                         ['"wpd"'], [wpd_0])
    u_err_0 = app_pd.u - app_ccm.u
    kavg_old = app_pd.k_avgs
    for runid in range(0, 1):
        print(f"### Runid= {runid}")
        app_pd.init_surface_correction()
        app_pd.clear()
        app_pd.export_to_tecplot(
            "peridynamic-after-correction" + f"{runid:02d}",
            *app_pd.provied_solutions)
        wpd_1 = app_pd.get_pd_elastic_energy_density()
        u_err_1 = app_pd.u - app_ccm.u
        app_pd.export_custom_data_to_tecplot(
            "peridynamic-energy-density" + f"{runid:02d}", ['"wpd"'], [wpd_1])
        app_pd.export_custom_data_to_tecplot(
            "peridynamic-displacement-error" + f"{runid:02d}",
            ['"Ux Before"', '"Uy Before"', '"Ux After"', '"Uy After"'],
            [u_err_0[:, 0], u_err_0[:, 1], u_err_1[:, 0], u_err_1[:, 1]])
        output_error(u_err_0, u_err_1, runid, grid_size, export_filename)
        output_kavg(kavg_old, app_pd.k_avgs, export_filename)
        kavg_old = app_pd.k_avgs
    print(f"Total time cost: {formatting_time(time.time() - t0)}")


if __name__ == "__main__":
    # 基础配置
    # meshtype          # 网格单元配置名 options: 1, 2, 3, 4, 5
    # constitutive      # 本构模型 options: "const", "exp"
    arg = argparse.ArgumentParser(f"python {sys.argv[0]}")
    arg.add_argument("-t",
                     "--mtype",
                     metavar="int",
                     default=1,
                     type=int,
                     help="mesh type of simulation")
    arg.add_argument("-c",
                     "--ctype",
                     metavar="str",
                     default="const",
                     type=str,
                     help="constitutive type")
    args = arg.parse_args()
    constitutive_mapping = {
        "const": ("A", "constant"),
        "exp": ("B", "attenuate")
    }
    c, cname = constitutive_mapping[args.ctype]
    example_name = f"example-A2{c}-{cname}"
    mesh_file_name = f"A2{args.mtype}.mesh"
    export_filename = example_name + ".out"
    main(example_name, mesh_file_name, cname, export_filename)
