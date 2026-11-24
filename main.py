"""WIP: calculate the total surface area of a mesh and print it to the
WIP terminal.

Debug mode (run directly, outside EP Workbench - see README.md) takes
the input mesh path and units as command-line arguments:

    python main.py <mesh_path> <mm2|cm2>
"""

# Boilerplate to run in debug mode or in EP Workbench WIP environment
try:
    case = cases[case_1]
    debug = False
except NameError:
    debug = True

# Mesh coordinates are in mm, so divide the mm² area by this to convert
UNIT_DIVISORS = {"mm2": 1, "cm2": 100}
UNIT_LABELS = {"mm2": "mm²", "cm2": "cm²"}


def _parse_debug_args():
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Debug-mode runner: print the surface area of a local "
                    "mesh file, outside EP Workbench."
    )
    parser.add_argument("mesh_path", type=Path, help="Path to the input surface mesh (.vtk)")
    parser.add_argument("units", choices=list(UNIT_DIVISORS), help="Units to print the area in")
    return parser.parse_args()


def main():

    # `case_name`/`units_name` (not `case_1`/`units`) deliberately, so that
    # assigning them in the debug branch can't shadow the `case_1`/`units`
    # globals the EP Workbench harness injects for the non-debug branch.
    if debug:
        import pyvista as pv

        args = _parse_debug_args()
        case_name = args.mesh_path.stem
        units_name = args.units
        mesh = pv.read(str(args.mesh_path))
    else:
        case_name = case_1
        units_name = units
        mesh = case.create_mesh()

    # Sum of all triangle areas, in the mesh's own units (mm for OpenEP cases)
    area = mesh.area / UNIT_DIVISORS[units_name]

    print(f"Surface area of '{case_name}': {area:.2f} {UNIT_LABELS[units_name]}")


if __name__ == "__main__":
    main()
