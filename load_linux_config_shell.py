import paramiko
import time 

# Create an SSH client object 
ssh_client = paramiko.SSHClient()

# Automatically add the server's host key to the local host keys file
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# define the connection parameters using a dictionary
linux = {'hostname':'10.193.41.83', 'port':'22','username':'user1','password':'eve'}
print(f'connecting to host {linux["hostname"]}')

# connect to service using method connect()
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

# invoke a shell session using the method invoke_shell()
shell = ssh_client.invoke_shell()

# send a command to the shell using the method send()
shell.send('cat /etc/passwd\n')
time.sleep(1)
shell.send('sudo cat /etc/shadow\n')
shell.send('eve\n')
time.sleep(1)

# receive the output of the command using the method recv()
output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

