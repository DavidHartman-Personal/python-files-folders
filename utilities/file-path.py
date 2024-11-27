
import os
import argparse
from pathlib import Path
from pprint import pp

# use suffixes if more than one suffix (e.g. .tar.gz) NOTE: returns an array
all_suffixes = Path('my/library.tar.gz').suffixes
# all_suffixes = ['.tar', '.gz']

# to create a single string with all extensions
# file_type_extension = join(all_suffixes.suffixes)
# file_type_extension = ".tar.gz"

# if there is no file/suffix, an empty array is returned.
all_suffixes_no_file = Path('my/library').suffixes
# all_suffixes = []

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

# Function that will list all files of a certain type for directory and child directories.


def recursive_iterdir(path: Path):
    items = []
    for item in path.iterdir():
        items.append(item)
        if item.is_dir():
            items.extend(recursive_iterdir(item))

    return items


def recursive_iterdir_gen(path: Path):
    for item in path.iterdir():
        yield item
        if item.is_dir():
            yield from recursive_iterdir_gen(item)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    #parser.add_argument('directory',type=str,help="The spreadsheet file to print the columns of")
    parser.add_argument('--start_dir',type=str,help="The spreadsheet file to print the columns of",nargs='?',default=ROOT_DIR, dest='start_dir')
    args = parser.parse_args()
    # Create a Path object
    starting_dir = Path(args.start_dir)
    pp(list(starting_dir.iterdir()))


    #get_spreadsheet_cols(args.input_file, print_cols=True)

if __name__ == "__main__":
    main()