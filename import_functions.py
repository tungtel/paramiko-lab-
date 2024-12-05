import myfunctions
import getpass
while True:
    password = getpass.getpass('Please enter your creds:')
    if password == 'cisco':
        print(f'password is correct')
        break
    else:
        print(f'password is not correct , please retype or contact admin')
        continue
r1 = {
    'server_ip': '10.123.2.1', 
    'port': '22', 
    'username':'u1', 
    'password':password, 
    'config':'ospf.txt'
    }

r2 = {
    'server_ip': '10.123.2.4', 
    'port': '22', 
    'username': 'u1', 
    'password': password, 
    'config':'eigrp.txt'
    }

r3 = {
    'server_ip': '10.123.2.5', 
    'port': '22', 
    'username': 'u1', 
    'password': password, 
    'config':'bgp.txt'
    }

valid_keys = ['server_ip','port','username','password']
routers = [r1,r2,r3]
new_routers = list()
for r in routers:
    new_r ={key:r[key] for key in valid_keys if key in r}
    # print(r["config"])
    connect_to_router = myfunctions.connect(**new_r)
    shell = myfunctions.get_shell(connect_to_router)
    myfunctions.send_from_file(shell,filename = r["config"],timeout = 2)
    output = myfunctions.show(shell,100000)
    print(output)
    myfunctions.close(connect_to_router)

