import click
from click import ClickException
import neoload_cli_lib.schema_validation as schema_validation


@click.command()
@click.option('--schema-url', help="The URL of the as-code schema. By default, use the one on Github", metavar="URL",
              default="https://raw.githubusercontent.com/Neotys-Labs/neoload-cli/master/resources/as-code.latest.schema.json")
@click.option('--refresh', is_flag=True, help="this options update schema from the web")
@click.argument('file')
def cli(file, refresh, schema_url):
    """Verify that the yaml FILE matches the neoload as-code file format"""
    try:
        schema_validation.validate_yaml(file, schema_url if refresh else None)
    except Exception as err:
        raise ClickException(str(err))
    print('Yaml file is valid.')
