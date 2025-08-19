#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Daniel Rode


import sys
from pathlib import Path

from geoai.download import download_naip


HELP_TEXT = "get-naip LONG_MIN LAT_MIN LONG_MAX LAT_MAX NAIP_YEAR DST_DIR"


try:
    bbox = sys.argv[1:5]
    naip_year = int(sys.argv[5])
    dst = Path(sys.argv[6])
except (IndexError, ValueError):
    print(HELP_TEXT)
    sys.exit(1)

dst.mkdir(exist_ok=True, parents=True)
download_naip(
    bbox,
    dst,
    year=naip_year,
    # The API gets mad if asked for a very large number of items
    max_items=999,
)
