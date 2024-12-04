import paramiko 
import time 
import getpass
from datetime import datetime

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

while True:
    try:
        password = getpass.getpass('Please enter the router creds:')
        router = {
            'hostname':'10.123.1.3',
            'port':22,
            'username':'u1',
            'password':password
            }
        ssh_client.connect(**router, look_for_keys = False , allow_agent = False)
        print(f'connected sucessfully to {router["hostname"]}')
        break
    except:
        print ('Authentication is failed , please retype the password')
        continue

shell = ssh_client.invoke_shell()
shell.send('terminal length 0 \n')
shell.send('enable\n')
shell.send('cisco\n')
shell.send('show running-config\n')
time.sleep(5)

output = shell.recv(100000).decode('utf-8')

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

filename = f'backup_{router["hostname"]}_{year}_{month}_{day}_{hour}_{minute}.txt'
with open(filename, 'w') as f:
    print(f'writing configuraiton to file')
    f.write(output)

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()



