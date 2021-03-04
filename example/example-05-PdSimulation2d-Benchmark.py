import numpy as np

import hmsolver.geometry as geometry
from hmsolver.app import PdSimulation2d
from hmsolver.basis import Quad4Node
from hmsolver.meshgrid import Zone2d, HybridMesh2d
from hmsolver.material import PdMaterial2d
from hmsolver.femcore import point_criteria, segment_criteria
from hmsolver.femcore import boundary_cond2d, BoundaryConds2d

import sys
import argparse

arg = argparse.ArgumentParser(f"python {sys.argv[0]}")
arg.add_argument("-p",
                 "--parallelized",
                 metavar="str",
                 default="True",
                 type=str,
                 help="open parallelized")
arg.add_argument("-s",
                 "--gridsize",
                 metavar="float",
                 default=0.1,
                 type=float,
                 help="grid size")

if __name__ == '__main__':
    args = arg.parse_args()
    args.parallelized = args.parallelized == "True"
    zone_xl, zone_xr = 0, 1
    zone_yl, zone_yr = 0, 1
    zone_xmid = 0.5 * (zone_xl + zone_xr)
    zone_ymid = 0.5 * (zone_yl + zone_yr)
    grid_size = args.gridsize
    zone = Zone2d(zone_xl, zone_xr, zone_yl, zone_yr)
    mesh2d = zone.meshgrid_zone(HybridMesh2d, grid_size)

    material2d = PdMaterial2d(3e11, 1.0 / 3)

    stretch = 0.1
    boundary_0 = point_criteria(zone_xmid, zone_yl)
    boundary_1 = segment_criteria(zone_xl, zone_yl, zone_xr, zone_yl)
    boundary_2 = segment_criteria(zone_xl, zone_yr, zone_xr, zone_yr)
    _bc_ = boundary_cond2d  # abbreviate the word for type & read
    boundarys = BoundaryConds2d(
        _bc_("point", boundary_0, "fixed", None, None),
        _bc_("segment", boundary_1, "set_uy", "constant", 0),
        _bc_("segment", boundary_2, "set_uy", "constant", +stretch))
    del _bc_  # delete the abbreviation
    boundarys.manually_verify()

    app = PdSimulation2d(mesh2d, material2d, boundarys)
    app.app_name = "plate"
    app.parallelized = args.parallelized
    horizon_radius, inst_len = 3 * grid_size, 0.015
    app.material.setPeridynamic(horizon_radius, grid_size, inst_len)
    app.mesh.peridynamic_construct(horizon_radius, 2 * horizon_radius,
                                   4 * horizon_radius)
    app.apply_basis(Quad4Node())
    app.check_engine()
    app.export_to_tecplot("peridynamic", *app.provied_solutions)
