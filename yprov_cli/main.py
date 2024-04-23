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
