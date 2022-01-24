import socket
import SPV

port = 2124
add = socket.gethostbyname(socket.gethostname())
print("You are on : ", add)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((add,port))
server.listen(1)

client, address = server.accept()

spv = SPV.SPV(server)

print(spv.Verify("password",client))

client.close()
