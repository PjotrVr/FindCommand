# FindCommand

FindCommand is a powerful search utility written in Python. It enables searching for directories, files, or both, within a specified start path.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Unit Tests](#unit-tests)
- [License](#license)

## Installation

To install FindCommand, open your PowerShell or Command Prompt in Administrator mode and run the following command:

```bash
.\install
```

## Usage

Available options:

    -d, --dir: Search for directories.
    -f, --file: Search for files.
    -df, --dirfile: Search for both files and directories. This is the default behavior.
    -cs, --case_sensitive: Make the search case sensitive to the passed name.
    --name: Specify a name pattern for files and directories.

Example:

```bash
Finder -f --name 'test' /path/to/search
```

This will search for files named 'test' in the directory /path/to/search.

## Configuration

You can configure the FindCommand tool through the config.json file. Here are the available configuration options:

    desiredPath: The path to your Python Scripts folder where the Finder command will be linked.
    commandName: The name of the command as you want it to appear in your terminal.

Example configuration:
```json
{
    "desiredPath": "Path/To/Your/Python/Scripts/Folder",
    "commandName": "Finder"
}
```

## Unit Tests

Unit tests are located in the tests/ directory. You can run these tests to verify the correctness of the code.

## License

This project is licensed under the terms of the MIT license. For more information, see the [LICENSE](LICENSE.md) file.