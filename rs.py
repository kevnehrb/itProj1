import socket as mysoc
import sys

rsListenPort = int(sys.argv[1])
dns = []

def createDict():
	inputFile = open("PROJI-DNSRS.txt","r")
	entries = inputFile.readlines()
	for i in entries:
		newEntry = i.split()
		dns.append(newEntry)
	inputFile.close()

def printDict():
	for entry in dns:
		print(entry)

def lookUp(hostname):
	found = False
	result = hostname
	for i in dns:
		for j in i:
			if hostname.lower() == j.lower():
				found = True
				result += " "+i[1]+" "+i[2]
	if not found:
		result += " - Error: HOST NOT FOUND"
	return result

def server():
	try:
		rss = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
		print("[C]: RS socket created")
	except mysoc.error as err:
		print('{} \n'.format("socket open error ", err))

	server_binding = ('', rsListenPort)
	rss.bind(server_binding)
	rss.listen(1)
	host = mysoc.gethostname()
	print("[S]: Server host name is: ", host)
	localhost_ip = (mysoc.gethostbyname(host))
	print("[S]: Server IP address is  ", localhost_ip)
	csockid, addr = rss.accept()
	print ("[S]: Got a connection request from a client at", addr)


createDict()
server()
lookUp("www.rutgers.")
