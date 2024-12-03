# import the necessary modules
import paramiko 
import time 
import getpass

ssh_client = paramiko.SSHClient()   #Create an instance of the SSHClient class
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())    #Set the policy to use when connecting to servers without a known host key

#Prompt the user to enter the password and store it in the variable password
password = getpass.getpass('Enter password: ')  

#Create a dictionary named router with the hostname, port, username and password of the router
router = {'hostname':'10.123.1.3', 'port':22, 'username':'u1', 'password':password}
print(f'connecting to router {router["hostname"]}')

#Connect to the router using the connect() method of the SSHClient class
ssh_client.connect(**router, look_for_keys = False, allow_agent = False)

#Invoke the shell using the invoke_shell() method of the SSHClient class
shell = ssh_client.invoke_shell()

#Send the commands to the router using the send() method of the shell object
shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('show ip int brief\n')

#Wait for 1 second before receiving the output of the commands
time.sleep(1)

#Receive the output of the commands using the recv() method of the shell object
output = shell.recv(10000)

#Decode the output from bytes to string and print it
output = output.decode('utf-8')
print(output)

# closing if the connection is open
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()
