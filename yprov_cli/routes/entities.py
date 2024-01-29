import typer
import requests
from typing_extensions import Annotated

from .utils.utils import get_data, parse_response, check_token, get_url

ROUTE = "entities"

app = typer.Typer(help="Operations on entities of a specific document")


@app.command('get')
def get_entity(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                   help="Name/ID of the document",
                                                   show_default=False,
                                                   rich_help_panel="Parameters")],
               e_id: Annotated[str, typer.Option("--e-id", "-e",
                                                 help="Name/ID of the entity",
                                                 show_default=False,
                                                 rich_help_panel="Parameters")]):
    """
    Get single entity.
    """
    token = check_token()

    response = requests.get(f"{get_url()}documents/{doc_id}/{ROUTE}/{e_id}?token={token}")

    parse_response(response, return_value=True)


@app.command('create')
def create_entity(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                      help="Name/ID of the document",
                                                      show_default=False,
                                                      rich_help_panel="Parameters")],
                  file: Annotated[str, typer.Option("--file", "-f",
                                                    help="File path of the entity file in JSON format",
                                                    show_default=False,
                                                    rich_help_panel="Mutually Exclusive")] = None,
                  value: Annotated[str, typer.Option("--value", "-v",
                                                     help="String with entity in JSON format",
                                                     show_default=False,
                                                     rich_help_panel="Mutually Exclusive")] = None):
    """
    Create new entity.
    """
    data = get_data(file, value)

    token = check_token()

    response = requests.post(f"{get_url()}documents/{doc_id}/{ROUTE}?token={token}", json=data)

    parse_response(response)


@app.command('update')
def update_entity(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                      help="Name/ID of the document",
                                                      show_default=False,
                                                      rich_help_panel="Parameters")],
                  e_id: Annotated[str, typer.Option("--e-id", "-e",
                                                    help="Name/ID of the entity",
                                                    show_default=False,
                                                    rich_help_panel="Parameters")],
                  file: Annotated[str, typer.Option("--file", "-f",
                                                    help="File path of the entity file in JSON format",
                                                    show_default=False,
                                                    rich_help_panel="Mutually Exclusive")] = None,
                  value: Annotated[str, typer.Option("--value", "-v",
                                                     help="String with entity in JSON format",
                                                     show_default=False,
                                                     rich_help_panel="Mutually Exclusive")] = None):
    """
    Update entity.
    """
    token = check_token()

    data = get_data(file, value)

    response = requests.put(f"{get_url()}documents/{doc_id}/{ROUTE}/{e_id}?token={token}", json=data)

    parse_response(response)


@app.command('delete')
def delete_entity(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                      help="Name/ID of the document",
                                                      show_default=False,
                                                      rich_help_panel="Parameters")],
                  e_id: Annotated[str, typer.Option("--e-id", "-e",
                                                    help="Name/ID of the entity",
                                                    show_default=False,
                                                    rich_help_panel="Parameters")]):
    """
    Delete single entity.
    """
    token = check_token()

    response = requests.delete(f"{get_url()}documents/{doc_id}/{ROUTE}/{e_id}?token={token}")

    parse_response(response)
