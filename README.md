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
