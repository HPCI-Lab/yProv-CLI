import typer
import requests
from typing_extensions import Annotated

from .utils.utils import get_data, parse_response, get_url, add_token

app = typer.Typer(help="User management")


@app.command('register')
def register(file: Annotated[str, typer.Option("--file", "-f",
                                               help="File path of the credentials in JSON format",
                                               show_default=False,
                                               rich_help_panel="Mutually Exclusive")] = None,
             value: Annotated[str, typer.Option("--value", "-v",
                                                help="String with credentials in JSON format",
                                                show_default=False,
                                                rich_help_panel="Mutually Exclusive")] = None):
    """
    Register a new user.

    Either a file or a string with the values must be passed
    """
    data = get_data(file, value)

    response = requests.post(f"{get_url()}auth/register", json=data)

    parse_response(response)


@app.command('login')
def login(file: Annotated[str, typer.Option("--file", "-f",
                                            help="File path of the credentials in JSON format",
                                            show_default=False,
                                            rich_help_panel="Mutually Exclusive")] = None,
          value: Annotated[str, typer.Option("--value", "-v",
                                             help="String with credentials in JSON format",
                                             show_default=False,
                                             rich_help_panel="Mutually Exclusive")] = None):
    """
    Login a user.

    Return the provided token and saves it in the config file if provided as an environment variable
    """
    data = get_data(file, value)

    response = requests.post(f"{get_url()}auth/login", json=data)

    parse_response(response, return_value=True)
    if response.ok:
        add_token(response)
