import socket
import SPV

port = 2124
add = socket.gethostbyname(socket.gethostname())
print("You are on : ", add)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostbyname(socket.gethostname()),port))

spv = SPV.SPV(client)

print(spv.GetVerified("password"))

client.close()
