# Autonomus Drone RPI

## Setting up the virtual environment

> Note : It is recommended to setup a virtual environment and then run the program
```bash
py -m venv ./venv  #creating virtual environment
venv\Scripts\activate  #to activate the environment after creation
```

## Installation and getting started

To install all the neccessary requirements run the following commands

```bash
pip install -r requirements.txt # for installation of libraries
```

## For running the program

Run the main.py file using

```bash
python main.py
```

## To Exclude files from github

To exclude files from github just add their path to the `.gitignore` file

## Adding new libraries to requirements file

To add more libraries to the `requiremnts.txt` file just install the library using pip/conda and then execute the following command in terminal

```bash
pip freeze > requirements.txt
```
## To upgrade a package already installed

```bash
pip install --upgrade --force-reinstall <package_name>
```