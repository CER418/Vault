import typer
from rich.console import Console
from rich.table import Table
from database import *
from model import Entry

console = Console()
app = typer.Typer()


@app.command(short_help="Insert a entry into vault.")
def add(name: str, username: str, password: str):
    typer.echo(f"Adding entry {name} to vault.")
    entry = Entry(name, username, password)
    insert_entry(entry)
    show()


@app.command(short_help="Remove a entry from vault.")
def remove(id: int):
    typer.echo(f"Deleting {id} from vault.")
    remove_entry(id)
    show()


@app.command(short_help="Update a entry in vault.")
def update(id: int, name: str, username: str, password: str):
    typer.echo(f"Updating {name} with id {id}.")
    update_entry(id, name, username, password)
    show()


@app.command(short_help="Display entries.")
def show():
    entries = get_all_entrys()
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#")
    table.add_column("Name", min_width=20, justify='center')
    table.add_column("Username", min_width=20, justify='center')
    table.add_column("Password", min_width=12, justify='center')
    table.add_column("Date added", min_width=12, justify='center')
    for index, entry in enumerate(entries, start=1):
        table.add_row(str(index), entry.name, entry.username, entry.password, entry.date)

    console.print(table)


if __name__ == '__main__':
    app()
