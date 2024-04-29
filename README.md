# yprov-cli

**yprov-cli** is one of the main components of the `yProv` service architecture: it provides a Command Line Interface to easily interact with the yProv Web Service front-end.


## Installation

You can install **yprov-cli** from **pip** using the build artifacts available under the `dist` folder:

```
pip install yprov_cli-1.0.0.tar.gz
```

Alternatively, you can use `poetry` to build and package the application on your own.

* Create a new conda environment with Python 3.9
```
conda create -n py39 python=3.9
conda activate py39
```

- Install poetry
```
pip install poetry
```

- Install dependencies from `pyproject.toml`
```
poetry install
```

- Build the application
```
poetry build
```

## Environment setup
Export the following environment variables to interact with a specific yProv instance
```console
$ export YPROV_ADDR=http://localhost
$ export YPROV_PORT=3000
```

## Usage

```console
$ yprov-cli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit. This option is available for every command.

**Commands**:
* `auth`: User management.
* `check`: Check if the service is active and running.
* `documents`: Operations on documents.

### `yprov-cli check`

Check if the service is active and running.

**Usage**:

```console
$ yprov-cli check [OPTIONS]
```

### `yprov-cli auth`

The `auth` command allows user registration and login.

**Usage**:

```console
$ yprov-cli auth [OPTIONS] COMMAND [ARGS]...
```

**Commands**:

* `register`: Register a new user.
* `login`: Login to the service.

##### `yprov-cli auth register`

Register a new user.

**Usage**:

```console
$ yprov-cli auth register [OPTIONS]
```

**Options**:

* `-u, --user TEXT`: User name, required
* `-p, --password TEXT`: User's password, required

##### `yprov-cli auth login`

Login to the service and get the token to perform any other request.

**Usage**:

```console
$ yprov-cli auth login [OPTIONS]
```

To user the token:
```console
$ export YPROV_TOKEN=[TOKEN]
```

**Options**:

* `-u, --user TEXT`: User name, required
* `-p, --password TEXT`: User's password, required

### `yprov-cli documents`

Operations on documents

**Usage**:

```console
$ yprov-cli documents [OPTIONS] COMMAND [ARGS]...
```

**Commands**:

* `create`: Create a new document.
* `delete`: Delete a document.
* `get`: Get documents.
* `permissions`: Manage user permissions for a specific DB.
* `subgraph`: Get the subgraph of a specific element identified by its ID.

##### `yprov-cli documents create`

Create a new document.

**Usage**:

```console
$ yprov-cli documents create [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the new document  [required]
* `-f, --file TEXT`: File path of the document file in JSON format
* `-v, --value TEXT`: String with document in JSON format. Use single quotes inside JSON to avoid conflict with the parsing of the string.

##### `yprov-cli documents delete`

Delete a document.

**Usage**:

```console
$ yprov-cli documents delete [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document to delete  [required]

##### `yprov-cli documents get`

Get documents.

If `doc_id` is provided, the content of a specific DB is returned, the list of all documents otherwise.

**Usage**:

```console
$ yprov-cli documents get [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: ID of the DB

##### `yprov-cli documents permissions`

Manage user permissions for a specific DB (only by the owner)

**Usage**:

```console
$ yprov-cli documents permissions [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the new document  [required]
* `-f, --file TEXT`: File path of the credentials in JSON format
* `-v, --value TEXT`: String with credentials in JSON format
* `-u, --user TEXT`: User name
* `-l, --level [r|w]`: permission you want to grant for a specific user
