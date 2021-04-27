import click

from dhis2_extractor import Dhis2Extractor


@click.group()
@click.option("--debug/--no-debug", default=False)
def cli(debug):
    click.echo("Debug mode is %s" % ("on" if debug else "off"))


@cli.command()
@click.argument("api_url")
@click.option("--username", "-u")
@click.option("--password", "-p")
@click.option(
    "--output-format", "-f", default=Dhis2Extractor.FORMAT_CSV, help="Only csv for now"
)
@click.option(
    "--output-path",
    "-o",
    help="An optional path to store the extracted data (use stdout if not provided)",
)
def extract(api_url, username, password, output_format, output_path):
    """Extract organisation units from a specific DHIS2 instance."""

    click.echo(f"Extracting org units for {api_url}")

    extractor = Dhis2Extractor(api_url, username=username, password=password)
    output = extractor.extract_organisation_units(
        output_format=output_format, output_path=output_path
    )
    if output is not None:
        click.echo(output)

    click.secho("Done.")


if __name__ == "__main__":
    cli()
