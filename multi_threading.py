import define_functions
import threading

def backup(router):
    client = define_functions.connect(**router)
    shell = define_functions.get_shell(client)
    define_functions.send_command(shell,'terminal length 0',1)
    define_functions.send_command(shell,'enable',1)
    define_functions.send_command(shell,'cisco',1)
    define_functions.send_command(shell,'show running-config',5)
    output = define_functions.show(shell)

    output_list = output.splitlines()
    output_list = output_list[19:-1]
    output =  '\n'.join(output_list)

    # print(output)

    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    filename = f'{router["server_ip"]}_{year}_{month}_{day}_{hour}_{minute}_{second}.txt'

    with open(filename,'w') as f:
        f.write(output)
        
    define_functions.close(client)

r1 = {'server_ip':'10.123.2.1', 'port':'22', 'username':'u1', 'password':'cisco'}
r4 = {'server_ip':'10.123.2.4', 'port':'22', 'username':'u1', 'password':'cisco'}
r5 = {'server_ip':'10.123.2.5', 'port':'22', 'username':'u1', 'password':'cisco'}
routers = [r1,r4,r5]

threads = list()

for router in routers:
    th = threading.Thread(target = backup, args = (router,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()
