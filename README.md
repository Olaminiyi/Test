import re
from collections import defaultdict

# Sample log data
log_data = """
12:10:10 serverIP: 10.3.4.5 UIR /home/website responseCode 400 TTL : 2200
12:10:10 serverIP: 10.3.4.4 UIR /home/website responseCode 200 TTL : 2000
12:10:10 serverIP: 10.3.4.5 UIR /home/website responseCode 400 TTL : 2000
"""

# Regular expression to match the server IP and response code
log_pattern = re.compile(r'serverIP: (?P<server_ip>\d+\.\d+\.\d+\.\d+).*responseCode (?P<response_code>\d+)')

# Dictionary to hold the count of each response code per server IP
server_response_count = defaultdict(lambda: defaultdict(int))

# Parse each line in the log data
for line in log_data.strip().split('\n'):
    match = log_pattern.search(line)
    if match:
        server_ip = match.group('server_ip')
        response_code = match.group('response_code')
        server_response_count[server_ip][response_code] += 1

# Display the results
for server_ip, codes in server_response_count.items():
    print(f"Server IP: {server_ip}")
    for code, count in codes.items():
        print(f"  Response Code {code}: {count} times")