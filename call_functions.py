import define_functions

# Define client as the return value of the connect() function
# Client is a instance of the SSHClient class
client = define_functions.connect('10.123.2.1','22','u1','cisco')

# Define shell as the return value of the get_shell() function
shell = define_functions.get_shell(client)

# Send the commands to the router using the send_command() function
define_functions.send_command(shell,'terminal length 0',2)

# Receive the output of the commands using the show() function
define_functions.show(shell)
define_functions.send_command(shell,'show ip interface brief',2)
define_functions.send_command(shell,'show version',2)

# Define output as the return value of the show() function
output = define_functions.show(shell)
print(output)

# Close the connection using the close() function
define_functions.close(client)
