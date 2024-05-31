import re
import pandas as pd
import matplotlib.pyplot as plt

with open("access.log", "r") as f:
    log_lines = f.readlines()

log_dicts = []

pattern = r'(?P<ip>\S+) - - \[(?P<datetime>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'

for line in log_lines:
    match = re.match(pattern, line)
    if match:
        log_parts = match.groupdict()
        log_dicts.append(log_parts)
    else:
        print("No match found for line:", line)

df = pd.DataFrame.from_dict(log_dicts)

df['status'] = df['status'].astype(int)
status_counts = df['status'].value_counts().sort_index()

# bar chart of IP status codes
plt.figure(figsize=(10, 6))
status_counts.plot(kind='bar')
plt.xlabel('Status Code')
plt.ylabel('Frequency')
plt.title('Frequency of Status Codes in Log File')
plt.show()

# IP frequency
ip_counts = df['ip'].value_counts()
ip_counts_df = ip_counts.reset_index()
ip_counts_df.columns = ['ip', 'count']
print(ip_counts_df)