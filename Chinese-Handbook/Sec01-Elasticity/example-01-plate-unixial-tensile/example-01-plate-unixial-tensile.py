import numpy as np
import time

from hmsolver.meshgrid import Zone2d
from hmsolver.meshgrid import Mesh2d
from hmsolver.material import Material2d
from hmsolver.femcore import point_criteria
from hmsolver.femcore import segment_criteria
from hmsolver.femcore import boundary_cond2d as _bc_  # abbreviation
from hmsolver.femcore import BoundaryConds2d
from hmsolver.app import Simulation2d
from hmsolver.basis import Quad4Node
from hmsolver.utils import formatting_time

if __name__ == '__main__':
    t0 = time.time()  # tic

    # 几何区域
    zone_xl, zone_xr = 0, 1
    zone_yl, zone_yr = 0, 1
    zone_xmid = 0.5 * (zone_xl + zone_xr)
    zone_ymid = 0.5 * (zone_yl + zone_yr)
    grid_num, grid_size = 50, 0.02
    zone = Zone2d(zone_xl, zone_xr, zone_yl, zone_yr)
    mesh2d = zone.meshgrid_zone_safe(Mesh2d, grid_num)
    n_nodes, n_elements = mesh2d.n_nodes, mesh2d.n_elements

    # 输出网格基本信息
    print(f"Mesh contains {n_nodes} nodes and {n_elements} elements.")
    print(f"Average Grid Size= {grid_size:.8f}")

    # 建立材料实例
    material2d = Material2d(300e9, 0.25)

    # 边界条件
    stretch = 0.02
    boundary_0 = point_criteria(zone_xmid, zone_yl)
    boundary_1 = segment_criteria(zone_xl, zone_yl, zone_xr, zone_yl)
    boundary_2 = segment_criteria(zone_xl, zone_yr, zone_xr, zone_yr)
    boundarys = BoundaryConds2d(
        _bc_("point", boundary_0, "fixed", None, None),
        _bc_("segment", boundary_1, "set_uy", "constant", 0),
        _bc_("segment", boundary_2, "set_uy", "constant", +stretch))
    boundarys.manually_verify()

    # 建立模拟实例
    app = Simulation2d(mesh2d, material2d, boundarys)
    app.app_name = "example-01-plate-unixial-tensile"
    app.apply_basis(Quad4Node())
    app.parallelized = True  # 开启并行多线程
    app.check_engine()

    # 输出模拟结果
    app.export_to_tecplot("elasticity", *app.provied_solutions)
    print(f"Total time cost: {formatting_time(time.time() - t0)}")