__version__ = '2019.09'
__author__ = 'David Hartman - PTC Cloud Security'
import sys
import os
import datetime

# This effectively defines the root of the project and so adding ..\, etc is not needed
# in config files,etc
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

# Add script directory to the path to allow searching for modules
sys.path.insert(0, PROJECT_ROOT_DIR)

import re

# Constants
###############################################################################

NAME_IP_MAPPING_FILE = "C:\\Users\\dhartman\\Documents\\FedRAMP\\ip-name-mapping.txt"
HEADER_ROW_FLAG = False
IN_FILE_FIELD_DELIMITER = "\t"
IP_DELIMITER = " "
OUT_FILE_FIELD_DELIMITER = "\t"


def datetime_handler(_input_datetime):
    if isinstance(_input_datetime, datetime.datetime):
        return _input_datetime.isoformat()
    raise TypeError('Unknown type')


# Main
###############################################################################
if __name__ == "__main__":
    # Open a tab delimited file and process each line
    try:
        with open(NAME_IP_MAPPING_FILE) as file_handle:
            line_number = 0
            for line in file_handle:
                line_number += 1
                if HEADER_ROW_FLAG and line_number == 1:
                    next(file_handle)
                else:
                    # If writing to a file then open it for writing now
                    name_ips = line.strip().split(IN_FILE_FIELD_DELIMITER)
                    name = name_ips[0]
                    all_ips = name_ips[1].split(IP_DELIMITER)
                    for ip in all_ips:
                        print(name, ip, sep=OUT_FILE_FIELD_DELIMITER)
                        # print("Line[" + str(line_number) + "]server:" + name + "\t" + ip)
    except Exception as e:
        print("Error in opening/processing file [{file}]: {exception}".format(file=NAME_IP_MAPPING_FILE,
                                                                              exception=str(e)))