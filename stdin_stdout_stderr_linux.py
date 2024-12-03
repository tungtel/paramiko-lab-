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

# execute a command on the remote server
stdin,stdout,stderr = ssh_client.exec_command('sudo adduser user3\n',get_pty=True)
stdin.write('eve\n')
stdin.write('eve\n')
time.sleep(1)

# print the output of the command
stdin,stdout,stderr = ssh_client.exec_command('cat /etc/passwd')
output = stdout.read().decode()
print(output)

# close the connection
if ssh_client.get_transport().is_active() == True:
    print('closing connection')
    ssh_client.close()
