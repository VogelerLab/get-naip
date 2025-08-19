# Author: Daniel Rode


FROM ghcr.io/opengeos/geoai:v0.6.0

COPY assets/get-naip.py /

USER root
ENTRYPOINT ["/opt/conda/bin/python", "/get-naip.py"]
