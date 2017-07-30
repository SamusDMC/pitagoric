#!/usr/bin/env bash

export PORT=${1:-'8080'}
export DEBUG='True'
export DEV='True'

python run.py
