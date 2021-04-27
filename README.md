# DHIS2 Extractor

This package provides utilities to extract [DHIS2](https://dhis2.org/) data.

## Installation

As the package is not published on Pypi yet, you can use `pip` to install the code of this repository:

```bash
pip install git+https://@github.com/blsq/dhis2_extractor.git
```

## Usage

### Using the command-line

This package provides a command-line tool for extraction operations:

```bash
dhis2_extractor extract https://play.dhis2.org/demo -u admin -p district -f csv -o output/test.csv
```

### Using Python code

Extracting organisation units can be done with the following code:

```python
from dhis2_extractor import Dhis2Extractor

extractor = Dhis2Extractor(
    "https://play.dhis2.org/demo", username="admin", password="district"
)
output = extractor.extract_organisation_units(output_format="csv")
```

## Docker

This package provides a `Dockerfile` to package the image. You can build the image locally using:

```bash
docker build -t blsq/dhis2_extractor:latest -t blsq/dhis2_extractor:0.x.x .
```

We also provide a GitHub workflow (see `.github/workflows/build_image.yml`) that is triggered either manually or 
when publishing a release.

The `docker-compose.yaml` file is meant for development: it will mount the repo root directory in the container.

```bash
docker-compose run app extract https://play.dhis2.org/demo -u admin -p district -f csv -o output/test.csv 
```

## Other remarks

We use `black` for code formatting (see [documentation](https://github.com/psf/black)).