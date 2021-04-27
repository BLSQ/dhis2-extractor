import csv

from dhis2_extractor import Dhis2Extractor


def test_extract_organisation_units(tmp_path):
    """Make sure that extract_organisation_units() creates a valid CSV file."""

    extractor = Dhis2Extractor(
        "https://play.dhis2.org/demo", username="admin", password="district"
    )
    output_path = tmp_path / "test.csv"
    extractor.extract_organisation_units(output_format="csv", output_path=output_path)

    with open(output_path) as output_csv:
        csv_reader = csv.reader(output_csv)
        header_row = next(csv_reader)
        assert isinstance(header_row, list)
        assert "id" in header_row

        first_row = next(csv_reader)
        assert isinstance(first_row, list)
