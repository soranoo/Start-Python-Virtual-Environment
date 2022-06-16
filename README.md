# Start-Python-Virtual-Environment
Project start on 25-11-2021 and spin off from my every project as a essential script on 09-02-2022

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Start virtual environment or create a new one automatically.

### Portal ↠ [Getting Started](#getting-started) ↞

## Features
* No more create/start virtual environment command needed.

## Requirements
* Python 3.6 or latest (*Developed in Python 3.8.1)

<a name="getting-started"></a>
## Getting Started
Clone the repository and run the `start-env.py`.
```
gh repo clone soranoo/Start-Python-Virtual-Environment
```

## TODO
* If the folder includes a file named `requirements.txt`, install the packages which inside the file automatically after the virtual environment is created.

## Known Issues
* Failed when folder included space ([issue #1](https://github.com/soranoo/Start-Python-Virtual-Environment/issues/1))

## Other Useful Commands
* Create `requirements.txt` - `pip freeze -l > requirements.txt`
* Install `requirements.txt` - `pip install -r requirements.txt`