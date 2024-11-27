"""Various functions for working on directories

These functions contain utilizes for analyzing directory/paths on an OS.

This file can also be imported as a module and contains the following
functions:

    * recursive_iterdir - returns a list of directories and subdirectories.
    * recursive_iterdir_gen - returns a list of directories and subdirectories as an iterative function
    * main - the main function of the script
"""
import os
import argparse
from pathlib import Path
from typing import List
from pprint import pp

# use suffixes if more than one suffix (e.g. .tar.gz) NOTE: returns an array
all_suffixes = Path('my/library.tar.gz').suffixes
# all_suffixes = ['.tar', '.gz']
filter_suffixes_default = [".py", ".md"]

# to create a single string with all extensions
# file_type_extension = join(all_suffixes.suffixes)
# file_type_extension = ".tar.gz"

# if there is no file/suffix, an empty array is returned.
all_suffixes_no_file = Path('my/library').suffixes
# all_suffixes = []

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

def recursive_iterdir(path: Path, filter_suffixes=None) -> list:
    """recursively iterates over the provided path location

    Args:
        filter_suffixes(list): An optional argument that contains a list of suffixes to filter
        path(Path): The starting directory path location

    Returns:
        items(List): A list of the directories
    """
    items = list()
    for item in path.iterdir():
        if filter_suffixes is None:
            items.append(item)
        else:
            if item.suffix in filter_suffixes:
                items.append(item)
        if item.is_dir():
            items.extend(recursive_iterdir(item, filter_suffixes))
    return items


def recursive_iterdir_gen(path: Path, filter_suffixes=None):
    """recursively iterates over the provided path location

    This function works as an iterative function that can be used in loops

    Args:
        filter_suffixes:
        path(Path): The starting directory path location
    """
    for item in path.iterdir():
        if filter_suffixes is None:
            yield item
        else:
            if item.suffix in filter_suffixes:
                yield item
        if item.is_dir():
            yield from recursive_iterdir_gen(item, filter_suffixes=filter_suffixes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    #parser.add_argument('directory',type=str,help="The spreadsheet file to print the columns of")
    parser.add_argument('--start_dir',type=str,help="The spreadsheet file to print the columns of",nargs='?',default=ROOT_DIR, dest='start_dir')
    args = parser.parse_args()
    # Create a Path object
    starting_dir = Path(args.start_dir)
    #pp(list(starting_dir.iterdir()))
    for files in recursive_iterdir_gen(starting_dir, filter_suffixes_default):
        print(files)
    pp(list(recursive_iterdir(starting_dir, filter_suffixes_default)))

if __name__ == "__main__":
    main()