#!/usr/bin/env bash

export DEBUG='True'
export PORT=${1:-'8080'}
export DEV='True'

python run.py
