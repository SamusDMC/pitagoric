#!/usr/bin/env bash

export DEBUG='True'
export PORT=${1:-'8080'}

python run.py
