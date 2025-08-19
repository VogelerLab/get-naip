# get-naip

Containerized CLI utility to download NAIP data for a given year and area.

## Usage

```sh
 podman run --rm --volume "$(pwd):$(pwd)" --workdir "$(pwd)" ghcr.io/vogelerlab/get-naip:main LONG_MIN LAT_MIN LONG_MAX LAT_MAX NAIP_YEAR DST_DIR
```
