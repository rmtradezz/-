#!/bin/bash
apt-get update && apt-get install -y libssl-dev libffi-dev build-essential
pip install -r requirements.txt
