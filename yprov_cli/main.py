from typing_extensions import Annotated

import typer
import os
import requests
import configparser
from .routes import (activities,
                     agents,
                     auth,
                     documents,
                     elements,
                     entities,
                     relations)

from .routes.utils.utils import get_url

config = configparser.ConfigParser()

app = typer.Typer()
app.add_typer(activities.app, name="activities", rich_help_panel="yProv Operations")
app.add_typer(agents.app, name="agents", rich_help_panel="yProv Operations")
app.add_typer(auth.app, name="auth", rich_help_panel="yProv Operations")
app.add_typer(documents.app, name="documents", rich_help_panel="yProv Operations")
app.add_typer(elements.app, name="elements", rich_help_panel="yProv Operations")
app.add_typer(entities.app, name="entities", rich_help_panel="yProv Operations")
app.add_typer(relations.app, name="relations", rich_help_panel="yProv Operations")


@app.callback()
def callback():
    """
    yProv-CLI service
    """


@app.command("check", rich_help_panel="General Operations")
def do_health_check():
    """
    Check if the service is active and running.
    """
    response = requests.get(get_url(prefix=False)+'/')
    if response.status_code == 200:
        typer.echo(response.text)
    else:
        typer.echo("Error!")


@app.command("config", rich_help_panel="General Operations")
def create_config(addr: Annotated[str, typer.Option("--addr", "-a",
                                                    help="Address of the service",
                                                    show_default=False)] = None,
                  port: Annotated[int, typer.Option("--port", "-p",
                                                    help="Port of the service",
                                                    show_default=False)] = None,
                  file: Annotated[str, typer.Option("--file", "-f",
                                                    help="Configuration file path",
                                                    show_default=False)] = None):
    """
    Configure yProv-CLI configuration file.

    If file is provided it will check if it is valid, otherwise if address and port are passed
    they will be written in the config file passed. If no file is provided it will be created only
    if the basic configuration are provided.

    If provided file already contains port and address of the service they can be omitted
    otherwise they must be specified.
    """

    if file or os.getenv("YPROV_CONFIG"):
        config.read(file)
        if 'YprovAddr' in config and 'YprovPort' in config:
            typer.echo("File valid!")
        else:
            if addr and port:
                config['DEFAULT'] = {'YprovAddr': addr, 'YprovPort': port}
                with open(file, 'w') as fp:
                    config.write(fp)
            else:
                typer.echo("Please pass both addr and port!", err=True)
    else:
        typer.echo("File not provided, creating a new one!")
        if addr and port:
            config['DEFAULT'] = {'YprovAddr': addr, 'YprovPort': port}
            with open('yprov_config.ini', 'w') as fp:
                config.write(fp)
        else:
            typer.echo("Please pass both addr and port!", err=True)
