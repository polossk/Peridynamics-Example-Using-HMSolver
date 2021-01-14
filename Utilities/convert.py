# mesh convertion
import glob
from hmsolver.femcore import convert_gmsh_into_msh


def main():
    files = glob.glob("*.msh")
    for file in files:
        convert_gmsh_into_msh(file, '.'.join(['.'.join(file.split('.')[:-1]), "mesh"]))


if __name__ == '__main__':
    main()
