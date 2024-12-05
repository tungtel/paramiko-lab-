import paramiko 
import getpass
import time 
import threading

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
threads = []

if __name__ == '__main__':
    for r in routers:
        th = threading.Thread(target = execute_command ,args = (r,'commands.txt'))
        threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()
