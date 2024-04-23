import typer
import requests
from typing_extensions import Annotated

from .utils.utils import get_data, parse_response, get_url

app = typer.Typer(help="User management")


@app.command('register')
def register(file: Annotated[str, typer.Option("--file", "-f",
                                               help="File path of the credentials in JSON format",
                                               show_default=False,
                                               rich_help_panel="Data (Mutually Exclusive)")] = None,
             value: Annotated[str, typer.Option("--value", "-v",
                                                help="String with credentials in JSON format",
                                                show_default=False,
                                                rich_help_panel="Data (Mutually Exclusive)")] = None,
             server_addr: Annotated[str, typer.Option("--server", "-s",
                                                      help="Server address",
                                                      show_default=False,
                                                      rich_help_panel="Connection Parameters")] = None,
             port_addr: Annotated[int, typer.Option("--port", "-p",
                                                    help="Server port",
                                                    show_default=False,
                                                    rich_help_panel="Connection Parameters")] = 3000,
             user: Annotated[str, typer.Option("--user", "-u",
                                               help="User name (must be specified along password)",
                                               show_default=False,
                                               rich_help_panel="Data (Mutually Exclusive)")] = None,
             password: Annotated[str, typer.Option("--password", "-x",
                                                   help="User's password (must be specified along user)",
                                                   show_default=False,
                                                   rich_help_panel="Data (Mutually Exclusive)")] = None):
    """
    Register a new user.

    Either a file or a string with the values must be passed
    """
    data = get_data(file, value, user, password)

    response = requests.post(f"{get_url()}auth/register", json=data)

    parse_response(response)


@app.command('login')
def login(file: Annotated[str, typer.Option("--file", "-f",
                                            help="File path of the credentials in JSON format",
                                            show_default=False,
                                            rich_help_panel="Data (Mutually Exclusive)")] = None,
          value: Annotated[str, typer.Option("--value", "-v",
                                             help="String with credentials in JSON format",
                                             show_default=False,
                                             rich_help_panel="Data (Mutually Exclusive)")] = None,
          server_addr: Annotated[str, typer.Option("--server", "-s",
                                                   help="Server address",
                                                   show_default=False,
                                                   rich_help_panel="Connection Parameters")] = None,
          port_addr: Annotated[int, typer.Option("--port", "-p",
                                                 help="Server port",
                                                 show_default=False,
                                                 rich_help_panel="Connection Parameters")] = 3000,
          user: Annotated[str, typer.Option("--user", "-u",
                                            help="User name (must be specified along password)",
                                            show_default=False,
                                            rich_help_panel="Data (Mutually Exclusive)")] = None,
          password: Annotated[str, typer.Option("--password", "-x",
                                                help="User's password (must be specified along user)",
                                                show_default=False,
                                                rich_help_panel="Data (Mutually Exclusive)")] = None):
    """
    Login a user.

    Return the provided token and saves it in the config file if provided as an environment variable
    """
    data = get_data(file, value, user, password)

    response = requests.post(f"{get_url()}auth/login", json=data)

    parse_response(response, return_value=True)
