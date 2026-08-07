# writing a python script to get the data from the API and print the name of the first user

import requests
response = requests.get('https://jsonplaceholder.typicode.com/users')
print('status code:', response.status_code)
users = response.json()
# print('users:', users[0]['name'])

# To save the output in a file as text

with open('users.txt', 'w') as file:
    for user in users:
        file.write(user['name'] + '\n')
