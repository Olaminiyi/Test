import re
from collections import defaultdict
from typing import List

def process_server_logs( data):

# Sample data content
# data = """
# 12:10:10 serverIP: 10.3.4.5 UIR /home/website responseCode 400 TTL : 2200
# 12:10:10 serverIP: 10.3.4.4 UIR /home/website responseCode 200 TTL : 2000
# 12:10:10 serverIP: 10.3.4.5 UIR /home/website responseCode 400 TTL : 2000
# """
    pattern = re.compile(r'serverIP: (?P<serverIP>\d+\.\d+\.\d+\.\d+).*responseCode (?P<responseCode>\d+)')

    newdata = data.strip().split('\n')
    serverResponse = defaultdict(int)

    for line in newdata:
        match = pattern.search(line)

        if match:
            serverIP = match.group('serverIP')
            responseCode = match.group('responseCode')
            serverResponse[(serverIP,responseCode)] += 1

    return serverResponse