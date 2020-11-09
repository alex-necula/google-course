#!/usr/bin/env python3

import re
import csv
import operator

error = {}
per_user = {}

# Creating the dictionaries
with open("syslog.log") as file:
    for line in file:
        if "ERROR" in line:
            match = re.search(r"ticky: ERROR ([\w' ]*) \(([\w\.]*)\)", line)

            error_name = match.group(1)
            if error_name not in error:
                error[error_name] = 1
            else:
                error[error_name] += 1
            
            username = match.group(2)
            if username not in per_user:
                per_user[username] = [0, 1] 
            else:
                per_user[username][1] += 1
        elif "INFO" in line:
            match = re.search(r"ticky: INFO [\w\[\]# ]* \(([\w\.]*)\)", line)
            username = match.group(1)
            if username not in per_user:
                per_user[username] = [1, 0]
            else:
                per_user[username][0] += 1

error = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
error.insert(0, ("Error", "Count"))

with open("error_message.csv", "w") as error_csv:
    writer = csv.writer(error_csv)
    writer.writerows(error)


per_user = sorted(per_user.items())
expanded_per_user = [["Username", "INFO", "ERROR"]]

for user in per_user:
    user = list(user)
    user.append(user[1][0])
    user.append(user[1][1])
    del user[1]
    expanded_per_user.append(user)

with open("user_statistics.csv", "w") as user_csv:
    writer = csv.writer(user_csv)
    writer.writerows(expanded_per_user)
    




        

