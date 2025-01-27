# PythonPackageCookiecutter# LiquidEngineCookiecutter

Python Package template made using [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)!

# How to use

## Install cookiecutter

```bash 
pip install cookiecutter
```

## Generate package folder structure

First, navigate to a folder where you want your package to live. 

```bash
cookiecutter https://github.com/HenriquesLab/PythonPackageCookiecutter
```

Cookiecutter will ask you for information regarding the package you want to create. 

After this step is complete a new folder will appear in your working directory. 

## Install the new package

First navigate to the newly created folder:

```bash
cd MyPackageFolder
pip install -e .
```

You now have a minimal working example of a Python Package. 

---