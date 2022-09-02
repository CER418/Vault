# Vault

## Description

A command line interface (CLI) vault for storing passwords and other information offline.

## Getting Started

### Installing

Install the necessary requirements by running `pip install requirements.txt`

### Executing program

All functions for CLI are listed in `python cli.py`

### Insert
Identifier can be anything, but I would recommend name or url.

`python cli.py insert <identifier> <username> <password>`

### Remove
Each entry in the database has a unique id.

`python cli.py remove <id>`

### Update
To update an entry in the database.

`python cli.py update <id> <value to update> <new value>`

### Display all entries in the database

`python cli.py show`

## Help

Any advice for common problems or issues.

`python cli.py --help`

## License

This project is licensed under the MIT License - see the LICENSE file for details.
