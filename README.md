# FindCommand

FindCommand is a powerful search utility written in Python. It enables searching for directories, files, or both, within a specified start path.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Unit Tests](#unit-tests)
- [Contribution](#contribution)
- [License](#license)

## Installation

To set up FindCommand on your local machine, open PowerShell/CMD in Administrator mode follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/PjotrVr/FindCommand.git
    ```
    or 
    
    ```bash
    git clone git@github.com:PjotrVr/FindCommand.git
    ```

2. Navigate into the project's root directory:

    ```bash
    cd FindCommand
    ```

3. Install the required dependencies by running the install script:

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


## Contribution

Contributions are always welcome! Here's how you can help:

1. Fork the repository to your own GitHub account by clicking the 'Fork' button at the top-right of the page.

2. Clone your forked repository to your local machine:

    ```bash
    git clone https://github.com/<YourUserName>/FindCommand.git
    ```

   Replace `<YourUserName>` with your actual GitHub username.

3. Install the required dependencies by running the install script:

    ```bash
    .\install
    ```

4. Make your changes. Remember to write unit tests for your changes in the `tests/` directory.

5. Commit and push your changes to your GitHub repository:

    ```bash
    git commit -m "Your descriptive commit message"
    git push
    ```

6. Create a pull request from your forked repository on GitHub.

Before creating a new pull request, please make sure that your code passes all unit tests.

Thank you for contributing!

## License

This project is licensed under the terms of the MIT license. For more information, see the [LICENSE](LICENSE.md) file.