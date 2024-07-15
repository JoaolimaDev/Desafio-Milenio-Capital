#!/bin/bash

# Install required packages
apk add --no-cache python3 py3-pip bash

# Create a virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install pandas

# Ensure the virtual environment's Python is used
export PATH="/app/venv/bin:$PATH"
