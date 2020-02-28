import socket as mysoc




def createDict():
    dns = []
    inputFile = open("PROJI-DNSTS.txt","r")
    inputFile.readlines()



def lookUp(hostname, dns):
    if hostname in dns:
        #check flag and return value based on that
    else:
        #return error string



def server():
    try:
        tss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: TS socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))

    server_binding=('',50007)
    tss.bind(server_binding)
    tss.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=tss.accept()
    print ("[S]: Got a connection request from a client at", addr)



createDict()
