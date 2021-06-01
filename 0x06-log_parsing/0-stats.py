#!/usr/bin/python3
import fileinput
import sys
import re


ip_01 = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."\
    r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."\
    r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."\
    r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

date = r"\[(\d{4})-(0[0-9]|(1[0-2]))-(3[01]|[12][0-9]|0[1-9]) ([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d+)\]"

status = r"(200|301|400|401|403|404|405|500)"
size = r" \d+"

my_regex = {
    "IP": ip_01,
    "datetime": date,
    "status": status,
    "size": size
}


message_final = '{IP} - {datetime} "GET /projects/260 HTTP/1.1" {status}{size}'
message_final = message_final.format(**my_regex)
print(message_final)
regex_search = re.search(
message_final, '236.31.22.245 - [2021-05-31 23:07:45.218905] "GET /projects/260 HTTP/1.1" 500 694')
print(regex_search)

for line in fileinput.input():
    print(line)
