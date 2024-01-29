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
    :param prefix: if prefix must be added to the base url
    :return:
    """
    if os.getenv("YPROV_CONFIG") or os.path.isfile("yprov_config.ini"):
        config_file = os.getenv("YPROV_CONFIG") if os.getenv("YPROV_CONFIG") else "yprov_config.ini"
        config = configparser.ConfigParser()
        config.read(config_file)
        addr = f"{config['DEFAULT']['YProvAddr']}:{config['DEFAULT']['YProvPort']}"
    elif os.getenv("YPROV_ADDR") and os.getenv("YPROV_PORT"):
        addr = f"{os.getenv('YPROV_ADDR')}:{os.getenv('YPROV_PORT')}"
    else:
        typer.echo("Service address not present. Please configure it!", err=True)
        raise typer.Abort

    if prefix:
        addr += PREFIX
    return addr


def get_data(file: str, value: str) -> dict:
    """
    Check the mutually exclusive parameters and return the contents as a dict
    :param file: file path
    :param value: json as a string
    :return:
    """
    if file is None and value is None:
        typer.echo("Please provide either a file or a value", err=True)
        raise typer.Abort
    elif file is not None and value is not None:
        typer.echo("Please provide either a file or a value", err=True)
        raise typer.Abort
    else:
        if file is not None:
            with open(file, 'r') as fp:
                return json.load(fp)
        else:
            return json.loads(value)


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
    if os.getenv("YPROV_CONFIG") or os.path.isfile("yprov_config.ini"):
        config_file = os.getenv("YPROV_CONFIG") if os.getenv("YPROV_CONFIG") else "yprov_config.ini"
        config = configparser.ConfigParser()
        config.read(config_file)
        if 'YProvToken' in config['DEFAULT']:
            return config['DEFAULT']['YProvToken']
        else:
            typer.echo("Token not present. Please log in!")
            raise typer.Abort
    elif os.getenv("YPROV_TOKEN"):
        return os.getenv("YPROV_TOKEN")
    else:
        typer.echo("Please specify token!")
        raise typer.Abort


def add_token(response: Response):
    """
    Add the token to the config file if it exists
    :param response: response object from the request
    :return:
    """
    token = response.json()["result"]
    if os.getenv("YPROV_CONFIG") or os.path.isfile("yprov_config.ini"):
        config_file = os.getenv("YPROV_CONFIG") if os.getenv("YPROV_CONFIG") else "yprov_config.ini"
        config = configparser.ConfigParser()
        config.read(config_file)
        config['DEFAULT']['YProvToken'] = token
        with open(config_file, 'w') as fp:
            config.write(fp)
