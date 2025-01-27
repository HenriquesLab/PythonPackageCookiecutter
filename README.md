# PythonPackageCookiecutter# LiquidEngineCookiecutter

Liquid Engine template made using [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)!

It helps create a python package and implements a simple class that subclasses the [Nanopyx Liquid Engine](https://github.com/HenriquesLab/NanoPyx).

### A video tutorial is available!
[![Video Tutorial](http://img.youtube.com/vi/s2SY6IlsWQI/0.jpg)](http://www.youtube.com/watch?v=s2SY6IlsWQI "How to Create a Python Package with the Liquid Engine")

# How to use

## Install cookiecutter

```bash 
pip install cookiecutter
```

## Generate package folder structure

First, navigate to a folder where you want your package to live. 

```bash
cookiecutter https://github.com/HenriquesLab/LiquidEngineCookieCutter
```

Cookiecutter will ask you for information regarding the package you want to create. 

After this step is complete a new folder will appear in your working directory. 

## Install the new package

First navigate to the newly created folder:

```bash
cd MyLiquidEngineFolder
pip install -e .
```

You now have a minimal working example of a Python Package. 

---