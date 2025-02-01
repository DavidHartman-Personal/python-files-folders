import click
import os


@click.command()
@click.option('--start', default=".", help='starting directory for search (default is current directory')
@click.option('--typ', default="*", help='filter for file types')
def find_files(start, typ):
    """search files in a directory optionally including a filter for file type"""
    click.echo(f"searching for files of {typ} starting in directory {start}")


if __name__ == "__main__":
    find_files()

