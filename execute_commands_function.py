import paramiko 
import getpass
import time 

def execute_command(router,filename):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'connecting to router {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys = False, allow_agent = False)
    shell = ssh_client.invoke_shell()
    with open(filename ,'r') as f:
        commands = f.readlines()
    for command in commands:
        shell.send(command)
    time.sleep(3)
    output = shell.recv(100000)
    print(output.decode('utf-8'))
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()

r1 = {
'hostname':'10.123.2.1',
'port':22,
'username':'u1',
'password':'cisco'
}

r4 = {
'hostname':'10.123.2.4',
'port':22,
'username':'u1',
'password':'cisco'
}

r5 = {
'hostname':'10.123.2.5',
'port':22,
'username':'u1',
'password':'cisco'
}

routers = [r1,r4,r5]

if __name__ == '__main__':
    for r in routers: 
        execute_command(r,filename = 'commands.txt')







