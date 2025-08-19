#!/usr/bin/env bash
# Author: Daniel Rode


set -e

cd "$(dirname "$0")"
podman build --tag get-naip .
