# `yprov-cli`

yProv-CLI service

**Usage**:

```console
$ yprov-cli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `activities`: Operations on activities of a specific...
* `agents`: Operations on agents of a specific document
* `auth`: User management
* `check`: Check if the service is active and running.
* `config`: Configure yProv-CLI configuration file.
* `documents`: Operations on documents
* `elements`: Operations on elements of a specific document
* `entities`: Operations on entities of a specific document
* `relations`: Operations on relations of a specific...

## `yprov-cli activities`

Operations on activities of a specific document

**Usage**:

```console
$ yprov-cli activities [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create`: Create new activity.
* `delete`: Delete single activity.
* `get`: Get single activity.
* `update`: Update activity.

### `yprov-cli activities create`

Create new activity.

**Usage**:

```console
$ yprov-cli activities create [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-f, --file TEXT`: File path of the activity file in JSON format
* `-v, --value TEXT`: String with activity in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli activities delete`

Delete single activity.

**Usage**:

```console
$ yprov-cli activities delete [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the activity  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli activities get`

Get single activity.

**Usage**:

```console
$ yprov-cli activities get [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the activity  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli activities update`

Update activity.

**Usage**:

```console
$ yprov-cli activities update [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the activity  [required]
* `-f, --file TEXT`: File path of the activity file in JSON format
* `-v, --value TEXT`: String with activity in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

## `yprov-cli agents`

Operations on agents of a specific document

**Usage**:

```console
$ yprov-cli agents [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create`: Create new agent.
* `delete`: Delete single agent.
* `get`: Get single agent.
* `update`: Update agent.

### `yprov-cli agents create`

Create new agent.

**Usage**:

```console
$ yprov-cli agents create [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-f, --file TEXT`: File path of the agent file in JSON format
* `-v, --value TEXT`: String with agent in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli agents delete`

Delete single agent.

**Usage**:

```console
$ yprov-cli agents delete [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the agent  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli agents get`

Get single agent.

**Usage**:

```console
$ yprov-cli agents get [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the agent  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli agents update`

Update agent.

**Usage**:

```console
$ yprov-cli agents update [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the agent  [required]
* `-f, --file TEXT`: File path of the agent file in JSON format
* `-v, --value TEXT`: String with agent in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

## `yprov-cli auth`

User management

**Usage**:

```console
$ yprov-cli auth [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `login`: Login a user.
* `register`: Register a new user.

### `yprov-cli auth login`

Login a user.

Return the provided token and saves it in the config file if provided as an environment variable

**Usage**:

```console
$ yprov-cli auth login [OPTIONS]
```

**Options**:

* `-f, --file TEXT`: File path of the credentials in JSON format
* `-v, --value TEXT`: String with credentials in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `-u, --user TEXT`: User name (must be specified along password)
* `-x, --password TEXT`: User's password (must be specified along user)
* `--help`: Show this message and exit.

### `yprov-cli auth register`

Register a new user.

Either a file or a string with the values must be passed

**Usage**:

```console
$ yprov-cli auth register [OPTIONS]
```

**Options**:

* `-f, --file TEXT`: File path of the credentials in JSON format
* `-v, --value TEXT`: String with credentials in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `-u, --user TEXT`: User name (must be specified along password)
* `-x, --password TEXT`: User's password (must be specified along user)
* `--help`: Show this message and exit.

## `yprov-cli check`

Check if the service is active and running.

**Usage**:

```console
$ yprov-cli check [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `yprov-cli documents`

Operations on documents

**Usage**:

```console
$ yprov-cli documents [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create`: Create a new document.
* `delete`: Delete a document.
* `get`: Get documents.
* `permissions`: Add user access to a specific DB.
* `subgraph`: Get subgraph of a specific element in...

### `yprov-cli documents create`

Create a new document.

**Usage**:

```console
$ yprov-cli documents create [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the new document  [required]
* `-f, --file TEXT`: File path of the document file in JSON format
* `-v, --value TEXT`: String with document in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli documents delete`

Delete a document.

**Usage**:

```console
$ yprov-cli documents delete [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document to delete  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli documents get`

Get documents.

If doc_id is provided it will return the content of that DB otherwise
it will return the list of all documents available

**Usage**:

```console
$ yprov-cli documents get [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: ID of the DB
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli documents permissions`

Add user access to a specific DB. Can be done only if owner of the DB. 

**Usage**:

```console
$ yprov-cli documents permissions [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the new document  [required]
* `-f, --file TEXT`: File path of the credentials in JSON format
* `-v, --value TEXT`: String with credentials in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `-u, --user TEXT`: User name (must be used along level)
* `-l, --level [o|r|w]`: User's level of permission that you want to grant (must be specified along user)
* `--help`: Show this message and exit.

### `yprov-cli documents subgraph`

Get subgraph of a specific element in specific document.

**Usage**:

```console
$ yprov-cli documents subgraph [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: ID of the element that contain the subgraph to extract  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

## `yprov-cli elements`

Operations on elements of a specific document

**Usage**:

```console
$ yprov-cli elements [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create`: Create new element.
* `delete`: Delete single element.
* `get`: Get single element.
* `update`: Update element.

### `yprov-cli elements create`

Create new element.

**Usage**:

```console
$ yprov-cli elements create [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-f, --file TEXT`: File path of the element file in JSON format
* `-v, --value TEXT`: String with element in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli elements delete`

Delete single element.

**Usage**:

```console
$ yprov-cli elements delete [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the element  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli elements get`

Get single element.

**Usage**:

```console
$ yprov-cli elements get [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the element  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli elements update`

Update element.

**Usage**:

```console
$ yprov-cli elements update [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the element  [required]
* `-f, --file TEXT`: File path of the element file in JSON format
* `-v, --value TEXT`: String with element in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

## `yprov-cli entities`

Operations on entities of a specific document

**Usage**:

```console
$ yprov-cli entities [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create`: Create new relation.
* `delete`: Delete single relation.
* `get`: Get single relation.
* `update`: Update relation.

### `yprov-cli entities create`

Create new relation.

**Usage**:

```console
$ yprov-cli entities create [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-f, --file TEXT`: File path of the entity file in JSON format
* `-v, --value TEXT`: String with entity in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli entities delete`

Delete single relation.

**Usage**:

```console
$ yprov-cli entities delete [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the entity  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli entities get`

Get single relation.

**Usage**:

```console
$ yprov-cli entities get [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the entity  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli entities update`

Update relation.

**Usage**:

```console
$ yprov-cli entities update [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the entity  [required]
* `-f, --file TEXT`: File path of the entity file in JSON format
* `-v, --value TEXT`: String with entity in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

## `yprov-cli relations`

Operations on relations of a specific document

**Usage**:

```console
$ yprov-cli relations [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create`: Create new relation.
* `delete`: Delete single relation.
* `get`: Get single relation.
* `update`: Update relation.

### `yprov-cli relations create`

Create new relation.

**Usage**:

```console
$ yprov-cli relations create [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-f, --file TEXT`: File path of the relation file in JSON format
* `-v, --value TEXT`: String with relation in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli relations delete`

Delete single relation.

**Usage**:

```console
$ yprov-cli relations delete [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the relation  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli relations get`

Get single relation.

**Usage**:

```console
$ yprov-cli relations get [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the relation  [required]
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.

### `yprov-cli relations update`

Update relation.

**Usage**:

```console
$ yprov-cli relations update [OPTIONS]
```

**Options**:

* `-d, --doc-id TEXT`: Name/ID of the document  [required]
* `-e, --e-id TEXT`: Name/ID of the relation  [required]
* `-f, --file TEXT`: File path of the relation file in JSON format
* `-v, --value TEXT`: String with relation in JSON format
* `-s, --server TEXT`: Server address
* `-p, --port INTEGER`: Server port
* `--help`: Show this message and exit.
