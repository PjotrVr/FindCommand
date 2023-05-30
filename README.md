# FindCommand

FindCommand is a custom implementation of the traditional 'find' command in Python. This project aims to provide users with an efficient and user-friendly way to search for files or directories on their system. The search process can be filtered using various parameters, making this utility extremely flexible and effective.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the latest version of Python.
* You have a `<Windows/Linux/Mac>` machine.

### Installation

Follow these steps to get a development environment running:

1. Clone the repository to your local machine:

git clone https://github.com/PjotrVr/FindCommand or git clone git@github.com:PjotrVr/FindCommand.git

2. Navigate to the project directory:

cd FindCommand

markdown


3. Install the required packages:

pip install -r requirements.txt

## Usage

Here's a brief overview of how you can use the FindCommand.

python find_command.py [-h] [-n NAME] [-t TYPE] [-p PATH]

Optional arguments:

-h, --help Show this help message and exit.
-n NAME, --name NAME Specify the name of the file or directory.
-t TYPE, --type TYPE Specify the type (file or directory).
-p PATH, --path PATH Specify the path in which to search.

## Contributing

If you want to contribute to `FindCommand`, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to the original branch: `git push origin <project_name>/<location>`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## License

This project uses the following license: [MIT License](<link>)