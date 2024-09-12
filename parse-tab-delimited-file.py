import io
import csv
import re
import requests

# Customer	Product	host name	Environment	OS
# Allegiant	SPM	ALGNT-TRVL101(App-Win) ALGNT-TRVL107(DB-Linux)	Prod	Linux
# BAYER CORPORATION	SKD	KNOW-LEDG01 (App/DB-Win) 	Prod	Other
# Beckman	SKD	KNOW-LEDG03 (App/DB-Win)	Prod	Other
# Bobcat Doosan	SPM	BBCT-DSAN103(App-Win) BBCT-DSAN104(DB-Linux)	Prod	Linux
# CNH	Content	Cont-stor05/Linux/Prod Cont-stor06/Linux/Prod Cont-stor07/Linux/Prod Cont-stor08/Linux/Prod Cont-stor09/Linux/Prod Cont-stor10/Linux/Prod Cont-stor15/Linux/Prod Cont-stor16/Win-Jump box/Prod Cont-stor17/Linux/Prod/ Cont-stor18//Linux/Prod cont-stor21/Linux/Prod Master DB Cont-stor22/Linux/Prod Slave DB	Prod	Linux

#
# aws_base_filename = "{file_basename}_{aws_account}_{YYYYMMDD}.json"
# aws_filename = aws_base_filename.format(f
#ile_basename="aws_ec2_instances",
#                                         aws_account=account_name,
#                                         YYYYMMDD=month_day_year)

# def datetime_handler(_input_datetime):
#     if isinstance(_input_datetime, datetime.datetime):
#         return _input_datetime.isoformat()
#     raise TypeError('Unknown type')


def process_host_field(host_field):
    hostname_regex = r"(\S+)\s*\((.+?)\)+"
    matches = re.finditer(hostname_regex, host_field, re.MULTILINE)
    # print("Processing field [{field}]".format(field=host_field))
    hosts_return = []
    for match in matches:
        # There should be 2 groups for each match
        host_type = {'HOST': match.group(1),
                     'TYPE': match.group(2)}
        hosts_return.append(host_type)
        # for group in match.groups():
        #     print(group)
    return hosts_return


if __name__ == "__main__":
    input_file = "C:\\Users\\dhartman\\Documents\\Anti-Virus\\Sophos\\Sophos-Deployment" \
                 "\\qts-servers-by-customer-product-environment-updated.txt"
    delimiter = "\t"

    try:
        with open(input_file) as tabfile:
            reader = csv.DictReader(tabfile, delimiter='\t')
            for row in reader:
                # Row contains Customer, Product, host name, Environment, OS
                customer = row['Customer']
                product = row['Product']
                cust_env = row['Environment']
                # returns an array of dictionary values for each server
                hosts_types = process_host_field(row['host name'])
                if len(hosts_types) == 0:
                    print(customer,
                          product,
                          cust_env,
                          row['host name'],
                          "INVALID HOST FIELD",
                          sep=delimiter)
                else:
                    for host_type in hosts_types:
                        print(customer,
                              product,
                              cust_env,
                              host_type['HOST'],
                              host_type['TYPE'],
                              sep=delimiter)
                # environment = row['Environment']
                # print("Customer: " + customer + " Env: " + cust_env)
    except Exception as e:
        print("Error in opening File: " + str(e))


# regex = r"(\S+)\((\S+)\)+"
# test_str = "ALGNT-TRVL101(App-Win) ALGNT-TRVL107(DB-Linux)"
# matches = re.finditer(regex, test_str, re.MULTILINE)
#
# for matchNum, match in enumerate(matches, start=1):
#     print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
#                                                                         end=match.end(), match=match.group()))
#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1
#         print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
#                                                                         end=match.end(groupNum),
#                                                                         group=match.group(groupNum)))

# def process_ps_info(process_info_file, server_id, server_name, header_flag):
#     # The output is assumed to be created using the following ps command line options
#     # ps -eo user,pid,ppid,start_time,args
#     # Flush any logging first
#     logging.getLogger().handlers[0].flush()
#     process_owner_re = re.compile(r"""\s*(\w+)  # Process Owner
#                                       \s*(\w+) # PID
#                                       \s*(\w+) # Parent PID
#                                       \s*([a-zA-Z0-9_:]+) # Start date/time
#                                       \s*(.*) # Rest of the line is the Command
#                                       """,
#                                   re.VERBOSE)
#     with open(process_info_file) as input_file_handle:
#         if (HEADER_ROW_FLAG): input_file_handle.readline()
#         lines = [line.rstrip('\n') for line in input_file_handle]
#         line_count = 0
#         for line in lines:
#             line_count += 1
#             string_match_groups = process_owner_re.match(line).groups()
#             process_owner = string_match_groups[0]
#             process_id = string_match_groups[1]
#             parent_process_id = string_match_groups[2]
#             start_time = string_match_groups[3]
#             command_string = string_match_groups[4]
#             has_arguments, trimmed_command = check_process_arguments(command_string)
#             logging.info("before [%s] and after [%s] has arguements? %r", command_string, trimmed_command, has_arguments)
