# onsimini-website
## Onsimini - The Gontran Sion personal website.
(Running on Python 3.8.1)

![workflow-status](https://github.com/onsimini/onsimini-website/workflows/build/badge.svg?branch=main)


## Description:
Basique 'Hello World!' flask page.

## install:
  * git clone the repo
  * python -m venv env
  * source env/bin/activate
  * pip install --upgrade pip
  * pip install -r requirements.txt
  * flask init-db
  * ( deactivate )

## run:
  * ( source env/bin/activate )
  * export FLASK_APP=run
  * flask run
  * open the URL (http://127.0.0.1:5000/)

## run test:
  * python -m pytest
  * flake8 website
  * flake8 test
