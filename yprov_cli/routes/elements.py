import typer
import requests
from typing_extensions import Annotated

from .utils.utils import get_data, parse_response, check_token, get_url

ROUTE = "elements"

app = typer.Typer(help="Operations on elements of a specific document")


@app.command('get')
def get_element(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                    help="Name/ID of the document",
                                                    show_default=False,
                                                    rich_help_panel="Parameters")],
                e_id: Annotated[str, typer.Option("--e-id", "-e",
                                                  help="Name/ID of the element",
                                                  show_default=False,
                                                  rich_help_panel="Parameters")],
                    server_addr: Annotated[str, typer.Option("--server", "-s",
                                                             help="Server address",
                                                             show_default=False,
                                                             rich_help_panel="Connection Parameters")] = None,
                    port_addr: Annotated[int, typer.Option("--port", "-p",
                                                           help="Server port",
                                                           show_default=False,
                                                           rich_help_panel="Connection Parameters")] = 3000):
    """
    Get single element.
    """
    token = check_token()

    header = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{get_url(server_addr, port_addr)}documents/{doc_id}/{ROUTE}/{e_id}", headers=header)

    parse_response(response, return_value=True)


@app.command('create')
def create_element(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                       help="Name/ID of the document",
                                                       show_default=False,
                                                       rich_help_panel="Parameters")],
                   file: Annotated[str, typer.Option("--file", "-f",
                                                     help="File path of the element file in JSON format",
                                                     show_default=False,
                                                     rich_help_panel="Data (Mutually Exclusive)")] = None,
                   value: Annotated[str, typer.Option("--value", "-v",
                                                      help="String with element in JSON format",
                                                      show_default=False,
                                                      rich_help_panel="Data (Mutually Exclusive)")] = None,
                    server_addr: Annotated[str, typer.Option("--server", "-s",
                                                             help="Server address",
                                                             show_default=False,
                                                             rich_help_panel="Connection Parameters")] = None,
                    port_addr: Annotated[int, typer.Option("--port", "-p",
                                                           help="Server port",
                                                           show_default=False,
                                                           rich_help_panel="Connection Parameters")] = 3000):
    """
    Create new element.
    """
    data = get_data(file, value)

    token = check_token()

    header = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{get_url(server_addr, port_addr)}documents/{doc_id}/{ROUTE}", headers=header, json=data)

    parse_response(response)


@app.command('update')
def update_element(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                       help="Name/ID of the document",
                                                       show_default=False,
                                                       rich_help_panel="Parameters")],
                   e_id: Annotated[str, typer.Option("--e-id", "-e",
                                                     help="Name/ID of the element",
                                                     show_default=False,
                                                     rich_help_panel="Parameters")],
                   file: Annotated[str, typer.Option("--file", "-f",
                                                     help="File path of the element file in JSON format",
                                                     show_default=False,
                                                     rich_help_panel="Data (Mutually Exclusive)")] = None,
                   value: Annotated[str, typer.Option("--value", "-v",
                                                      help="String with element in JSON format",
                                                      show_default=False,
                                                      rich_help_panel="Data (Mutually Exclusive)")] = None,
                    server_addr: Annotated[str, typer.Option("--server", "-s",
                                                             help="Server address",
                                                             show_default=False,
                                                             rich_help_panel="Connection Parameters")] = None,
                    port_addr: Annotated[int, typer.Option("--port", "-p",
                                                           help="Server port",
                                                           show_default=False,
                                                           rich_help_panel="Connection Parameters")] = 3000):
    """
    Update element.
    """
    token = check_token()

    data = get_data(file, value)

    header = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{get_url(server_addr, port_addr)}documents/{doc_id}/{ROUTE}/{e_id}", headers=header, json=data)

    parse_response(response)


@app.command('delete')
def delete_element(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                       help="Name/ID of the document",
                                                       show_default=False,
                                                       rich_help_panel="Parameters")],
                   e_id: Annotated[str, typer.Option("--e-id", "-e",
                                                     help="Name/ID of the element",
                                                     show_default=False,
                                                     rich_help_panel="Parameters")],
                    server_addr: Annotated[str, typer.Option("--server", "-s",
                                                             help="Server address",
                                                             show_default=False,
                                                             rich_help_panel="Connection Parameters")] = None,
                    port_addr: Annotated[int, typer.Option("--port", "-p",
                                                           help="Server port",
                                                           show_default=False,
                                                           rich_help_panel="Connection Parameters")] = 3000):
    """
    Delete single element.
    """
    token = check_token()

    header = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{get_url(server_addr, port_addr)}documents/{doc_id}/{ROUTE}/{e_id}", headers=header)

    parse_response(response)
