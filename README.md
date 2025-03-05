# Python Project Template

Template for quick python project setup.

Once you have cloned this repository, you will need to attend to a few files. The main ones will be the `pyproject.toml` file, and the top-level folder in the `src` directory. You should rename this to whatever you want your project to be called, and make sure to update the project name in the `pyproject.toml` file. The placeholder names chosen here (`package_name` and `module`) are not usually natural choices for anything in a project directory. It should be straightforward enough to find all instances of this nomenclature in this template project and replace it with whatever you want to call your package/module.

## Installation

### Creating `venv`

#### Windows

At first usage, create virtual environment (specify  whatever verion of Python you want your `venv` to use):

```bash
py -3.XX -m venv <environment-name, e.g. '.venv.'>
```

Then activate (need to do this every time you reopen the terminal):

```bash
./.venv/Scripts/activate
```

#### Linux

At first usage, create virtual environment (specify  whatever verion of Python you want your `venv` to use):

```bash
python3.XX -m venv <environment-name, e.g. '.venv.'>
```

Then activate (need to do this every time you reopen the terminal):

```bash
source ./.venv/bin/activate
```

### Package install

At first usage, make sure `pip` is up to date:

```bash
python -m pip install --upgrade pip
```

Use `deactivate` to leave the virtual environment.

Lastly, install the `package_name` package in editable mode:

```bash
pip install -e .
```

You can now simply import the `package_name` package by including the following in your Python scripts:

```bash
from package_name import <submodule> as <namespace>
```

### Installing optional packages

Optional packages include:

- Documentation[^1]: `doc`
- Your optional package[^1]: `optional_package_name`

Install with

```bash
pip install -e .[optional_package_name1,optional_package_name2,etc.]
```

### Building documentation

You will need to install the package with the `doc` option, i.e.,

```bash
pip install -e .[doc]
```

Then either use the `Makefile` or `make.bat` to compile the documentation in whatever format you want.

[^1]: Installs packages necessary to make documentation with Sphinx.
