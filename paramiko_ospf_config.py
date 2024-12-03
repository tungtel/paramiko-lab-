# import the necessary modules
import paramiko 
import time 
import getpass

ssh_client = paramiko.SSHClient()   #Create an instance of the SSHClient class
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())    #Set the policy to use when connecting to servers without a known host key

#Prompt the user to enter the password and store it in the variable password
password = getpass.getpass('Enter password: ')  

#Create a dictionary for the router with the hostname, port, username, and password
r1 = {'hostname':'10.123.2.1', 'port':22, 'username':'u1', 'password':password}
r4 = {'hostname':'10.123.2.4', 'port':22, 'username':'u1', 'password':password}
r5 = {'hostname':'10.123.2.5', 'port':22, 'username':'u1', 'password':password}

#Create a list of the routers
routers = [r1,r4,r5]

#Iterate over the routers in the list
for routers in routers:
    
    print(f'connecting to router {routers["hostname"]}')
    #Connect to the router using the connect() method of the SSHClient class
    ssh_client.connect(**routers, look_for_keys = False, allow_agent = False)

    #Invoke the shell using the invoke_shell() method of the SSHClient class
    shell = ssh_client.invoke_shell()

    #Send the commands to the router using the send() method of the shell
    shell.send('enable\n')
    shell.send('cisco\n')
    shell.send('terminal length 0\n')
    shell.send('configure terminal\n')
    shell.send('router ospf 1\n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('show ip ospf neighbor\n')
    shell.send('show ip ospf interface brief\n')
    shell.send('show ip protocols\n')

    #Wait for 2 seconds
    time.sleep(2)
    
    #Receive the output from the router using the recv() method of the shell
    output = shell.recv(10000).decode('utf-8')
    print(output)

# closing if the connection is open
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()
