import typer
import requests
from typing_extensions import Annotated
from enum import Enum
from .utils.utils import get_data, parse_response, check_token, get_url

app = typer.Typer(help="Operations on documents")


@app.command('get')
def get_docs(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                 help="ID of the DB",
                                                 show_default=False)] = None:
    """
    Get documents.

    If doc_id is provided it will return the content of that DB otherwise
    it will return the list of all documents available
    """
    req_url = f"{get_url()}documents"
    if doc_id:
        req_url += f"/{doc_id}"

    token = check_token()

    header = {"Authorization": f"Bearer {token}"}
    response = requests.get(req_url, headers=header)

    parse_response(response, return_value=True)


@app.command('subgraph')
def get_docs(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                 help="Name/ID of the document",
                                                 show_default=False,
                                                 rich_help_panel="Parameters")],
             e_id: Annotated[str, typer.Option("--e-id", "-e",
                                               help="ID of the element that contain the subgraph to extract",
                                               show_default=False,
                                               rich_help_panel="Parameters")]:
    """
    Get subgraph of a specific element in specific document.


    """
    req_url = f"{get_url()}documents/{doc_id}/subgraph"

    token = check_token()

    header = {"Authorization": f"Bearer {token}"}
    response = requests.get(req_url+f"?id={e_id}", headers=header)

    parse_response(response, return_value=True)


@app.command('create')
def create_doc(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                   help="Name/ID of the new document",
                                                   show_default=False,
                                                   rich_help_panel="Parameters")],
               file: Annotated[str, typer.Option("--file", "-f",
                                                 help="File path of the document file in JSON format",
                                                 show_default=False,
                                                 rich_help_panel="Data (Mutually Exclusive)")] = None,
               value: Annotated[str, typer.Option("--value", "-v",
                                                  help="String with document in JSON format",
                                                  show_default=False,
                                                  rich_help_panel="Data (Mutually Exclusive)")] = None:
    """
    Create a new document.
    """
    data = get_data(file, value)

    token = check_token()

    header = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{get_url()}documents/{doc_id}", headers=header, json=data)

    parse_response(response)


@app.command('delete')
def delete_doc(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                   help="Name/ID of the document to delete",
                                                   show_default=False,
                                                   rich_help_panel="Parameters")]:
    """
    Delete a document.
    """
    token = check_token()

    header = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{get_url()}documents/{doc_id}", headers=header)

    parse_response(response)


class Permissions(str, Enum):
    o = "o"
    r = "r"
    w = "w"


@app.command('permissions')
def add_user_to_doc(doc_id: Annotated[str, typer.Option("--doc-id", "-d",
                                                        help="Name/ID of the new document",
                                                        show_default=False,
                                                        rich_help_panel="Parameters")],
                    file: Annotated[str, typer.Option("--file", "-f",
                                                      help="File path of the credentials in JSON format",
                                                      show_default=False,
                                                      rich_help_panel="Data (Mutually Exclusive)")] = None,
                    value: Annotated[str, typer.Option("--value", "-v",
                                                       help="String with credentials in JSON format",
                                                       show_default=False,
                                                       rich_help_panel="Data (Mutually Exclusive)")] = None,
                    user: Annotated[str, typer.Option("--user", "-u",
                                                      help="User name (must be used along level)",
                                                      show_default=False,
                                                      rich_help_panel="Data (Mutually Exclusive)")] = None,
                    level: Annotated[Permissions, typer.Option("--level", "-l",
                                                               help="User's level of permission that you want to "
                                                                    "grant (must be specified along user)",
                                                               show_default=False,
                                                               rich_help_panel="Data (Mutually Exclusive)")] = None):
    """
    Add user access to a specific DB. Can be done only if owner of the DB. 
    """
    token = check_token()

    data = get_data(file, value, user, level) #=level.value)

    header = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{get_url()}documents/{doc_id}/permissions", headers=header, json=data)

    parse_response(response)
