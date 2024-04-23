import json
import os
import typer
import configparser
from requests import Response

PREFIX = "/api/v0/"


def get_url(prefix: bool = True) -> str:
    """
    Returns the url of the service.
    Before any other choice check if a config file is present otherwise check for environment variables
    :param address: server address
    :param port: server port
    :param prefix: if prefix must be added to the base url
    :return:
    """
    if os.getenv("YPROV_ADDR") and os.getenv("YPROV_PORT"):
        addr = f"{os.getenv('YPROV_ADDR')}:{os.getenv('YPROV_PORT')}"
    else:
        typer.echo("Service address not present. Please configure it!", err=True)
        raise typer.Abort

    if prefix:
        addr += PREFIX
    return addr


def get_data(file: str, value: str, user: str = None, password: str = None, level: str = None) -> dict:
    """
    Check the mutually exclusive parameters and return the contents as a dict
    :param level: level of permission requested
    :param password: user password
    :param user: user's name
    :param file: file path
    :param value: json as a string
    :return:
    """
    if level:
        passed_values = True if user else False
    else:
        passed_values = True if password and user else False

    # Check for mutual exclusivity between the three methods to pass information
    if (file is None and value is None and not passed_values) or \
            (file is None and value is not None and passed_values) or \
            (file is not None and value is not None and passed_values) or \
            (file is not None and value is None and passed_values) or \
            (file is not None and value is not None and not passed_values):
        typer.echo("Please provide either a file, a JSON string or both user and password parameters", err=True)
        raise typer.Abort
    else:
        if file is not None:
            with open(file, 'r') as fp:
                return json.load(fp)
        elif value is not None:
            return json.loads(value)
        elif level is not None:
            return {"user": user, "level": level}
        else:
            return {"user": user, "password": password}


def parse_response(resp: Response, return_value: bool = False):
    """
    Parse the response and return the content of the response alongside the status code for error messages
    :param resp: response object from the request
    :param return_value: if the request should have returned a value
    :return:
    """
    if resp.status_code == 200 or resp.status_code == 201:
        if return_value:
            typer.echo(resp.json()['result'], color=True)
        else:
            typer.echo(resp.json()['message'], color=True)
    else:
        typer.echo(f"{resp.status_code} : {resp.json()['error']}", err=True)


def check_token() -> str:
    """
    Check if the token is specified
    :return:
    """
    if os.getenv("YPROV_TOKEN"):
        return os.getenv("YPROV_TOKEN")
    else:
        typer.echo("Please specify token!")
        raise typer.Abort
