#!/bin/bash
rm -f bigben.zip
rm -rf venv
virtualenv --python=python3.6 venv
source venv/bin/activate
pip3 install -r requirements.txt
deactivate
cd venv/lib/python3.6/site-packages/
zip -r9 ../../../../bigben.zip .
cd ../../../../
zip -g bigben.zip -r *.py images

