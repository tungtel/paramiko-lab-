#import the necessary libraries
import paramiko
import time 

# Define the function connect() that takes the server_ip, port, username and password as arguments
# This function will return an object
def connect(server_ip, port, username,password):
    #Create an instance of the SSHClient class
    ssh_client = paramiko.SSHClient()  
    #Set the policy to use when connecting to servers without a known host key
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
    print(f'connecting to router {server_ip}')
    #Connect to the router using the connect() method of the SSHClient class
    ssh_client.connect(hostname=server_ip, port=port, username=username, password=password, look_for_keys = False, allow_agent = False)
    #Return the ssh_client object
    return ssh_client

# Define the function get_shell() that takes the ssh_client object as an argument
# This function will return an object
def get_shell(ssh_client):
    #Invoke the shell using the invoke_shell() method of the SSHClient class
    shell = ssh_client.invoke_shell()
    #Return the shell object
    return shell

# Define the function send_command() that takes the shell, command and timeout as arguments
# This fuction will perform a task. 
def send_command(shell, command, timeout = 1):
    print(f'Sending command: {command}')
    #Send the commands to the router using the send() method of the shell object
    shell.send(command + '\n')
    time.sleep(timeout)

def send_from_list(shell, list_of_commands , timeout = 2):
    print(f'sending command from the list')
    for command in list_of_commands:
        shell.send(command + '\n')
    time.sleep(timeout)

def send_from_file(shell,filename,timeout = 2):
    print(f'Sending config from a file')

    with open(filename,'r') as f:
        commands = f.readlines()

    for command in commands:
        shell.send(command)
    time.sleep(timeout)

# Define the function show() that takes the shell and n as arguments
# This function will return a result 
def show(shell , n = 100000):
    #Receive the output of the commands using the recv() method of the shell object
    output = shell.recv(n)
    #Decode the output from bytes to string and return it
    return output.decode('utf-8')

# Define the function close() that takes the ssh_client object as an argument
# This function will perfom a task which close the session. 
def close(ssh_client):
    # check if the connection is open by calling the get_transport() method of the ssh_client object
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        #Close the connection using the close() method of the ssh_client object
        ssh_client.close()

if __name__ == '__main__':
    #Define r1 as a dictionary with the hostname, port, username and password of the router
    r1 = {
        'server_ip':'10.123.2.1', 
        'port':22, 
        'username':'u1', 
        'password':'cisco'
        }
    #Connect to the router using the connect() function
    client = connect(**r1)
    #Invoke the shell using the get_shell() function
    shell = get_shell(client)

    #Define a filename & call the predefined function
    filename = 'rip.txt'
    send_from_file(shell,filename,timeout = 2)

    #Receive the output of the commands using the show() function
    output = show(shell)

    #Print the output
    print(output)

    #close the connection
    close(client)
