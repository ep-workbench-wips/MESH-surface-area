# Surface Area

Calculate the total surface area of a mesh and print it to the WIP
terminal.

## Prerequisites

- **Conda** (or your preferred Python environment) is installed.
- (Recommended) EP Workbench, minimal version `v1.1.0-beta.1-260505`. Download instructions available [here](https://openep.discourse.group/t/downloading-ep-workbench-beta-for-academic-use/149).

## Setting up an environment

EP Workbench passes cases to a WIP as pickled OpenEP `Case` objects, so the
Python environment used as the WIP interpreter must have the
[OpenEP library](https://github.com/ecci-cvs/openep-py) installed. The WIP
itself needs nothing beyond OpenEP and its dependencies. Choose one of the
options below.

### Option 1: use an existing OpenEP environment

If you already have an environment with OpenEP installed (e.g. the one set
up for [atrial_regionalisation](https://github.com/arnovonkietzell/atrial_regionalisation)),
you can use it as-is. Check that OpenEP imports, then save the interpreter
path:

```bash
conda activate <your_openep_env>
python -c "import openep"
which python #save this env python path for later
```

### Option 2: create a dedicated environment

```bash
conda create -n surface_area python=3.10 pip
conda activate surface_area
git clone https://github.com/ecci-cvs/openep-py
cd openep-py
python -m pip install -e .
python -c "import openep"
which python #save this env python path for later
```

If you only want to run the WIP in debug mode (outside EP Workbench),
PyVista is enough:

```bash
conda create -n surface_area_debug python=3.10 pip
conda activate surface_area_debug
pip install pyvista
```

## Running this WIP through EP Workbench

- Open EP Workbench and navigate to Work-in-Progress > Marketplace.
- Select "Surface Area" and press "clone".
- On the WIP Bar, select Info > Edit.
- Set Interpreter as the path to your python environment (from above), and
  Root Dir as the path to this `surface_area` folder. Save these settings
  and close the WIP editor window.
- Select any surface mesh as the input (`case_1`) and run the WIP.
- Set the `units` widget to `mm2` or `cm2`.
- The total surface area (the sum of all triangle areas) is printed to the
  WIP terminal in the chosen units, assuming the mesh coordinates are in mm.
- No output case is created.

## Running this WIP outside EP Workbench

Debug mode takes the input mesh path and units as command-line arguments;
the case name is inferred from the filename stem:

```bash
conda activate surface_area
cd surface_area
python main.py /path/to/mesh.vtk cm2
```
