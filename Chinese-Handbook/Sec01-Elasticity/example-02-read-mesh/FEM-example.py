import numpy as np
import time

from hmsolver.meshgrid import Zone2d
from hmsolver.meshgrid import Mesh2d
from hmsolver.material import Material2d
from hmsolver.femcore import read_mesh_to_MeshObject
from hmsolver.femcore import point_criteria
from hmsolver.femcore import segment_criteria
from hmsolver.femcore import boundary_cond2d as _bc_  # abbreviation
from hmsolver.femcore import BoundaryConds2d
from hmsolver.femcore import get_deform_mesh
from hmsolver.app import Simulation2d
from hmsolver.basis import Quad4Node
from hmsolver.utils import formatting_time

APP_NAME = "FEM-example"
MESH_FILE_NAME = "FEM-example.mesh"

if __name__ == '__main__':
    t0 = time.time()  # tic
    # 几何区域
    zone_xl, zone_xr = -2, 2
    zone_yl, zone_yr = -1, 1
    zone_xmid = 0.5 * (zone_xl + zone_xr)
    zone_ymid = 0.5 * (zone_yl + zone_yr)

    # 网格配置
    mesh2d = read_mesh_to_MeshObject(MESH_FILE_NAME, Mesh2d)
    n_nodes, n_elements = mesh2d.n_nodes, mesh2d.n_elements
    total_area = (zone_yr - zone_yl) * (zone_xr - zone_xl)
    pores_area = np.pi * 0.08**2 * 120
    grid_size = np.sqrt((total_area - pores_area) / n_elements)

    # 输出网格基本信息
    print(f"Mesh contains {n_nodes} nodes and {n_elements} elements.")
    print(f"Average Grid Size= {grid_size:.8f}")

    # 建立材料实例
    material2d = Material2d(300, 0.25)

    # 边界条件
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

    # 建立模拟实例
    app = Simulation2d(mesh2d, material2d, boundarys_ccm)
    app.app_name = APP_NAME
    app.parallelized = True
    app.apply_basis(Quad4Node())
    app.check_engine()

    # 输出模拟结果及运行时间
    app.export_to_tecplot("elasticity", *app.provied_solutions)
    app.mesh.nodes = get_deform_mesh(app.mesh.nodes, app.u, deform_scale_factor=1.0)
    app.export_to_tecplot("elasticity-deform", *app.provied_solutions)
    # restore and re-deform
    app.mesh.nodes = get_deform_mesh(app.mesh.nodes, app.u, deform_scale_factor=-1.0)
    app.mesh.nodes = get_deform_mesh(app.mesh.nodes, app.u, deform_scale_factor=5.0)
    app.export_to_tecplot("elasticity-deform-5x", *app.provied_solutions)

    print(f"Total time cost: {formatting_time(time.time() - t0)}")
