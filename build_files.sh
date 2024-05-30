#!/bin/bash

echo "BUILD START"

# Ensure Python 3.11 is available and install dependencies
if command -v python3.11 &> /dev/null
then
    echo "Python 3.11 is available"
else
    echo "Python 3.11 is not available. Exiting..."
    exit 1
fi

python3.11 -m pip install --upgrade pip
python3.11 -m pip install -r requirements.txt

# Collect static files
python3.11 manage.py collectstatic --noinput --clear

echo "BUILD END"
