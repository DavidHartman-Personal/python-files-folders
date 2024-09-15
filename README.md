# Python file-ulities

This repository contains various scripts, libraries, etc. for working with directory structures, including searching 
files, printing directory trees, etc.

Echo folder in this project includes a single ptyhon script command line progam along with a bash wrapper script

## bash interaction

In order to call python command line scripts in bash as a single command call a wrapper bash script must be written 
to make the call to python.

E.g.

To run a python script without including bash wrapper would be:

`python3 python-script`

Done with a bash wrapper this would become

`python-script`

Wrapping a bash shell script would be:

```bash
#!/bin/bash

# Run the Python script in the background
python3 ./find-files.py

```

Another option would be to create bash alias to make the call.  E.g. 

`alias pythonscript='python ./pythonscript.py`

So each folder will contain the python srcipt along with a bash shell script to make python call.