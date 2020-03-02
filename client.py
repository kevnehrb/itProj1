import socket as mysoc
import sys

rsHostName = sys.argv[1]
rsListenPort = int(sys.argv[2])
tsListenPort = int(sys.argv[3])

try:
    socket1 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    print("[C]: socket1 created")
except mysoc.error as err:
    print('{} \n'.format("socket1 open error ", err))

try:
    socket2 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    print("[C]: socket2 created")
except mysoc.error as err:
    print('{} \n'.format("socket2 open error ", err))

socketHostName = mysoc.gethostbyname(mysoc.gethostname())


# connect socket 1
socket1ServerBinding = (socketHostName, tsListenPort)
socket1.connect(socket1ServerBinding)
print("socket1 connected to ts")

# connect socket 2
socket2ServerBinding = (socketHostName, rsListenPort)
socket2.connect(socket2ServerBinding)
print("socket2 connected to rs")

socket1.close()
socket2.close()
exit()