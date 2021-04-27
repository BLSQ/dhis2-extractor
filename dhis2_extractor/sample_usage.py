from dhis2_extractor import Dhis2Extractor

extractor = Dhis2Extractor(
    "https://play.dhis2.org/demo", username="admin", password="district"
)
output = extractor.extract_organisation_units(
    output_format="csv", output_path="output/sample.csv"
)
print("Done")
