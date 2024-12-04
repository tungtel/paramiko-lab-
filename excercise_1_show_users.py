#Write a script do follwing fuctions : 
#1. Connect to a router using paramiko
#2. Prompt the user to enter the password
#3. If the authentication is successful, print "connected successfully to <hostname>"
#4. If the authentication is failed, print "Authentication failed, please retype the password"
#5. If the connection is successful, invoke the shell
#6. Send the command "show users" to the router and output result 
#7. Close the connection if it is open

import paramiko
import time
import getpass

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
        break #break out from the loop 
    except:
        print ('Authentication is failed , please retype the password')
        continue

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show users\n')
time.sleep(2)

output = shell.recv(100000)
print(output.decode('utf-8'))

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()




  
       
  

