# DEVASC Code Examples

This repository contains code examples for the DevNet Associate training courseware.

You can clone this repo locally to work within your own development environment.

The `master` branch contains the blank files that you can fill in during the course.

The `solutions` branch contains the working code.

The `src` folder contains code examples for all the hands-on exercises so you can try them in your own development environment. 

This code requires Python3. The [requirements.txt](./requirements.txt) file lists all the dependencies required by the code used in the course. Follow the instructions below to setup a local developerment environment that matches the in-browser development environment used in the course.

## Get a local copy of the code

1. Clone to repo, e.g., `git clone https://github.com/CiscoDevNet/devasc-code-examples.git`
2. `cd devasc-code-examples/`
   
## Setup Python Virtual Environment

### MacOS or Linux

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
        
### Windows - recommendation to use git-bash terminal

1. `py -3 -m venv venv`
2. `source venv/Scripts/activate`
3. `pip install -r requirements-win.txt`
