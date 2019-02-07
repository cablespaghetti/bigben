#!/bin/sh
cd venv/lib/python3.6/site-packages/
zip -r9 ../../../../bigben.zip .
cd ../../../../
zip -g bigben.zip -r *.py images

