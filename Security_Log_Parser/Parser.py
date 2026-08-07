with open('Sample.log', 'r') as file:
    logs = file.readlines()
print('Suspicious logs:\n') 
for log in logs:
    if 'ERROR' in log or 'WARNING' in log:
        print(log.strip())