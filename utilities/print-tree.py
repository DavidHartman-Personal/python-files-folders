import click
import os
from pathlib import Path
from itertools import islice

space = '    '
branch = '│   '
tee = '├── '
last = '└── '
indentation = 4


@click.command()
@click.option('--start', default=".", help='starting directory for search (default is current directory')
@click.option('--typ', default="*", help='filter for file types')
# def print_tree(start, typ):
#     """search files in a directory optionally including a filter for file type"""
#     click.echo(f"searching for files of {typ} starting in directory {start}")
#     for root, dirs, files in os.walk(start):
#         level = root.replace(start, '').count(os.sep)
#         indent = ' ' * 4 * level
#         print('{}{}/'.format(indent, os.path.basename(root)))
#         subindent = ' ' * 4 * (level + 1)
#         for f in files:
#             print('{}{}'.format(subindent, f))
# def printtree(start, typ, level: int = -1, limit_to_directories: bool = False,
#               length_limit: int = 1000):
#     """Given a directory Path object print a visual tree structure"""
#     dir_path = Path(start)  # accept string coerceable to Path
#     files = 0
#     directories = 0
#
#     def inner(dir_path: Path, prefix: str = '', level=-1):
#         nonlocal files, directories
#         if not level:
#             return  # 0, stop iterating
#         if limit_to_directories:
#             contents = [d for d in dir_path.iterdir() if d.is_dir()]
#         else:
#             contents = list(dir_path.iterdir())
#         pointers = [tee] * (len(contents) - 1) + [last]
#         for pointer, path in zip(pointers, contents):
#             if path.is_dir():
#                 yield prefix + pointer + path.name
#                 directories += 1
#                 extension = branch if pointer == tee else space
#                 yield from inner(path, prefix=prefix + extension, level=level - 1)
#             elif not limit_to_directories:
#                 yield prefix + pointer + path.name
#                 files += 1
#
#     print(dir_path.name)
#     iterator = inner(dir_path, level=level)
#     for line in islice(iterator, length_limit):
#         print(line)
#     if next(iterator, None):
#         print(f'... length_limit, {length_limit}, reached, counted:')
#     print(f'\n{directories} directories' + (f', {files} files' if files else ''))
#
#
# def showFolderTree(path, show_files=False, indentation=2, file_output=False):
#     """
#     Shows the content of a folder in a tree structure.
#     path -(string)- path of the root folder we want to show.
#     show_files -(boolean)-  Whether or not we want to see files listed.
#                             Defaults to False.
#     indentation -(int)- Indentation we want to use, defaults to 2.
#     file_output -(string)-  Path (including the name) of the file where we want
#                             to save the tree.
#     """
#
#     tree = []
#
#     if not show_files:
#         for root, dirs, files in os.walk(path):
#             level = root.replace(path, '').count(os.sep)
#             indent = ' ' * indentation * (level)
#             tree.append('{}{}/'.format(indent, os.path.basename(root)))
#
#     if show_files:
#         for root, dirs, files in os.walk(path):
#             level = root.replace(path, '').count(os.sep)
#             indent = ' ' * indentation * (level)
#             tree.append('{}{}/'.format(indent, os.path.basename(root)))
#             for f in files:
#                 subindent = ' ' * indentation * (level + 1)
#                 tree.append('{}{}'.format(subindent, f))
#
#     if file_output:
#         output_file = open(file_output, 'w')
#         for line in tree:
#             output_file.write(line)
#             output_file.write('\n')
#     else:
#         # Default behaviour: print on screen.
#         for line in tree:
#             print
#             line
#
def walkdir(start, typ):
    """Print a directory tree

      print dir tree..e.g.
        print-tree.py
                print-tree.sh
        root_dir_test/
            print-tree.py
            level1/
            level2/
                print-tree.sh
            level3/
                level4/


      Parameters:
        start (<String>) : starting directory
        typ (<String>) : Filter for file types

      Returns
        None

      Raises
        IOError: An error occurred accessing the smalltable.
      """
    # f"{project_name}" if export_path is None else export_path
    if typ is None:
        print("Found None")
        file_name_filter = ""
    else:
        file_name_filter = "." + typ
    abs_start_path = os.path.abspath(start)
    print("print directory tree starting at:", abs_start_path)
    print("filter for files of type:", file_name_filter)

    tree = []
    for root, dirs, files in os.walk(start):
        # print(root, dirs, files)
        level = root.replace(start, '').count(os.sep)
        indent = ' ' * indentation * level
        print("root:", root)
        print("dirs:", dirs)
        print("files:", files)
        print("level:", level)
        # print("Creating tree\n\n")
        if not files:
            print("Found a dir:", dirs)
            for direct in dirs:
                print(''.join([indent, direct]))
        else:
            for file in files:
                print("Found file:", file)
                # check the extension of files
                # if file.endswith(file_name_filter):
                    # print whole path of files
                    # print(os.path.join(root, file))
                print(''.join([indent,file]))


if __name__ == "__main__":
    walkdir()
