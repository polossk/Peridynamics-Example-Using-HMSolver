import zipfile
import os

import numpy as np

import hmsolver.geometry as geometry
from hmsolver.app import CrackSimulation2d
from hmsolver.basis import Quad4Node
from hmsolver.meshgrid import Zone2d, HybridMesh2d
from hmsolver.material import PdMaterial2d
from hmsolver.femcore import point_criteria, segment_criteria
from hmsolver.femcore import boundary_cond2d, BoundaryConds2d
from hmsolver.femcore.preprocessing import read_mesh

if __name__ == '__main__':
    zone_xl, zone_xr = 0, 0.2
    zone_yl, zone_yr = 0, 0.1
    zone_xmid = 0.5 * (zone_xl + zone_xr)
    zone_ymid = 0.5 * (zone_yl + zone_yr)
    grid_size = 0.0015
    horizon_radius = 0.0045
    inst_len = 0.0005
    zone = Zone2d(zone_xl, zone_xr, zone_yl, zone_yr)

    input_file = 'data_2100_2000.msh'
    if not os.path.exists(input_file):
        zip_archive = 'data_2100_2000.zip'
        if not os.path.exists(zip_archive):
            raise Exception('no available data found.')
        else:
            ziphandle = zipfile.ZipFile('data_2100_2000.zip', 'r')
            ziphandle.extract(input_file)
    n_nodes, n_elements, nodes, elements = read_mesh(input_file)
    mesh2d = HybridMesh2d(n_nodes, n_elements)
    mesh2d.manually_construct(np.array(nodes), np.array(elements))

    material2d = PdMaterial2d(3e11, 1.0 / 3)

    stretch = 0.002
    boundary_0 = point_criteria(zone_xl, zone_ymid)
    boundary_1 = segment_criteria(zone_xl, zone_yl, zone_xl, zone_yr)
    boundary_2 = segment_criteria(zone_xr, zone_yl, zone_xr, zone_yr)
    _bc_ = boundary_cond2d  # abbreviate the word for type & read
    boundarys = BoundaryConds2d(
        _bc_("point", boundary_0, "fixed", None, None),
        _bc_("segment", boundary_1, "set_ux", "constant", 0),
        _bc_("segment", boundary_2, "set_ux", "constant", stretch))
    del _bc_  # delete the abbreviation
    boundarys.manually_verify()

    app = CrackSimulation2d(mesh2d, material2d, boundarys)
    app.app_name = "plate"
    horizon_radius, inst_len = 0.0045, 0.0005
    app.material.setPeridynamic(horizon_radius, grid_size, inst_len)
    app.material.stretch_crit = 20
    app.mesh.peridynamic_construct(horizon_radius, 2 * horizon_radius,
                                   4 * horizon_radius)
    app.apply_basis(Quad4Node())
    app.check_engine()

    app.detect_failure(0.95 * np.max(app.w_dis))
    app.update_mesh()
    app.run_simulation(1)

    app.export_to_tecplot("hybrid", *app.provied_solutions)
