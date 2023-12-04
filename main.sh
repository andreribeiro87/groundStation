#!/usr/bin/env bash

# assert that the script is running in the project root
python3 -m http.server 8000 --bind 0.0.0.0

python3 main.py

firefox 0.0.0.0:8000/teste.html