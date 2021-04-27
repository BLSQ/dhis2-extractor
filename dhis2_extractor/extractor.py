from dhis2 import Api, RequestException
import pandas as pd


class Dhis2ExtractorException(Exception):
    """It's always a good practice to define our own exceptions, as they can be targeted in except clauses."""

    pass


class Dhis2Extractor(object):
    """This class fetches DHIS2 data using the dhis2 library and outputs it in various formats."""

    FORMAT_CSV = "csv"

    def __init__(self, url, *, username, password):
        # Let's re-use an existing library instead of maintaining our own
        self._api = Api(url, username, password)

    def extract_organisation_units(self, *, fields=":all", output_format, output_path):
        """
        Extract organisation units.

        Methods should always expose parameters subject to changes, such as field names and output options.

        :param fields:
        :param output_format:
        :param output_path:
        :return:
        """

        try:
            response_data = self._api.get_paged(
                "organisationUnits", params={"fields": fields}, merge=True
            )
        except RequestException as e:  # Always handle exceptions
            raise Dhis2ExtractorException(
                # Prefer f-strings to concatenation / string interpolation
                f"An error occurred while fetching DHIS2 data (URL: {e.url}, status code: {e.code})"
            )

        organisation_units = response_data["organisationUnits"]
        dataframe = pd.DataFrame.from_dict(organisation_units)

        return self._dump(
            dataframe, output_format=output_format, output_path=output_path
        )

    def _dump(self, dataframe, *, output_format, output_path):
        if output_format == self.FORMAT_CSV:
            return dataframe.to_csv(output_path)

        raise NotImplementedError(f'Unknown output format "{output_format}"')
