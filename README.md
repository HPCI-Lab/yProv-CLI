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
$ yprov-cli activities create [OPTIONS] DOC_ID
```

**Arguments**:

* `DOC_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli activities delete`

Delete single activity.

**Usage**:

```console
$ yprov-cli activities delete [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli activities get`

Get single activity.

**Usage**:

```console
$ yprov-cli activities get [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli activities update`

Update activity.

**Usage**:

```console
$ yprov-cli activities update [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
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
$ yprov-cli agents create [OPTIONS] DOC_ID
```

**Arguments**:

* `DOC_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli agents delete`

Delete single agent.

**Usage**:

```console
$ yprov-cli agents delete [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli agents get`

Get single agent.

**Usage**:

```console
$ yprov-cli agents get [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli agents update`

Update agent.

**Usage**:

```console
$ yprov-cli agents update [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
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

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--user TEXT`
* `--password TEXT`
* `--help`: Show this message and exit.

### `yprov-cli auth register`

Register a new user.

Either a file or a string with the values must be passed

**Usage**:

```console
$ yprov-cli auth register [OPTIONS]
```

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--user TEXT`
* `--password TEXT`
* `--help`: Show this message and exit.

## `yprov-cli check`

Check if the service is active and running.

**Usage**:

```console
$ yprov-cli check [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `yprov-cli config`

Configure yProv-CLI configuration file.

If file is provided it will check if it is valid, otherwise if address and port are passed
they will be written in the config file passed. If no file is provided it will be created only
if the basic configuration are provided.

If provided file already contains port and address of the service they can be omitted
otherwise they must be specified.

**Usage**:

```console
$ yprov-cli config [OPTIONS]
```

**Options**:

* `--addr TEXT`
* `--port INTEGER`
* `--file TEXT`
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

* `add-user`: Add user access to a specific DB.
* `create`: Create a new document.
* `delete`: Delete a document.
* `get`: Get documents.

### `yprov-cli documents add-user`

Add user access to a specific DB. Can be done only if owner of the DB. 

**Usage**:

```console
$ yprov-cli documents add-user [OPTIONS] DOC_ID
```

**Arguments**:

* `DOC_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--user TEXT`
* `--level [o|r|w]`
* `--help`: Show this message and exit.

### `yprov-cli documents create`

Create a new document.

**Usage**:

```console
$ yprov-cli documents create [OPTIONS] DOC_ID
```

**Arguments**:

* `DOC_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli documents delete`

Delete a document.

**Usage**:

```console
$ yprov-cli documents delete [OPTIONS] DOC_ID
```

**Arguments**:

* `DOC_ID`: [required]

**Options**:

* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
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

* `--doc-id TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
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
$ yprov-cli elements create [OPTIONS] DOC_ID
```

**Arguments**:

* `DOC_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli elements delete`

Delete single element.

**Usage**:

```console
$ yprov-cli elements delete [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli elements get`

Get single element.

**Usage**:

```console
$ yprov-cli elements get [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli elements update`

Update element.

**Usage**:

```console
$ yprov-cli elements update [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
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
$ yprov-cli entities create [OPTIONS] DOC_ID
```

**Arguments**:

* `DOC_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli entities delete`

Delete single relation.

**Usage**:

```console
$ yprov-cli entities delete [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli entities get`

Get single relation.

**Usage**:

```console
$ yprov-cli entities get [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli entities update`

Update relation.

**Usage**:

```console
$ yprov-cli entities update [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
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
$ yprov-cli relations create [OPTIONS] DOC_ID
```

**Arguments**:

* `DOC_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli relations delete`

Delete single relation.

**Usage**:

```console
$ yprov-cli relations delete [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli relations get`

Get single relation.

**Usage**:

```console
$ yprov-cli relations get [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.

### `yprov-cli relations update`

Update relation.

**Usage**:

```console
$ yprov-cli relations update [OPTIONS] DOC_ID E_ID
```

**Arguments**:

* `DOC_ID`: [required]
* `E_ID`: [required]

**Options**:

* `--file TEXT`
* `--value TEXT`
* `--server-addr TEXT`
* `--port-addr INTEGER`: [default: 3000]
* `--help`: Show this message and exit.
