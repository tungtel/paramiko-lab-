import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

while True:
    try:
        password = getpass.getpass('Please enter the router creds:')
        router = {
            'hostname':'10.123.2.1',
            'port':22,
            'username':'u1',
            'password':password
            }
        ssh_client.connect(**router, look_for_keys = False , allow_agent = False)
        print(f'connected sucessfully to {router["hostname"]}')
        break #break out from the loop 
    except:
        print ('Authentication is failed , please retype the password')
        continue
commands = [
    'enable', 'cisco', 'conf t', 
    'username admin1 secret cisco', 
    'access-list 1 permit any', 'end', 
    'terminal length 0', 
    'sh run | i user'
    ]

shell = ssh_client.invoke_shell()
for command in commands: 
    shell.send(command + '\n')
time.sleep(5)

output = shell.recv(100000)
print(output.decode('utf-8'))

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()
