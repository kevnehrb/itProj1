import socket as mysoc
import sys

tsListenPort = int(sys.argv[1])
dns = []

def createDict():
	inputFile = open("PROJI-DNSTS.txt","r")
	entries = inputFile.readlines()
	for i in entries:
		newEntry = i.split()
		dns.append(newEntry)
	inputFile.close()

def printDict():
	for entry in dns:
		print(entry)

def lookUp(hostname):
	print("looking up hostname: " + hostname)
	found = False
	result = hostname
	for i in dns:
		print("comparing {} with {}".format(hostname, i[0]))
		if hostname.lower() == i[0].lower():
			print("match found")
			result += " "+i[1]+" "+i[2]
			found = True
			break
	if not found:
		print("match not found")
		result += " - Error: HOST NOT FOUND"
	return result

def server():
	try:
		tss = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
		print("[C]: TS socket created")
	except mysoc.error as err:
		print('{} \n'.format("socket open error ", err))

	server_binding = ('', tsListenPort)
	tss.bind(server_binding)
	tss.listen(1)
	host = mysoc.gethostname()
	print("[S]: Server host name is: ", host)
	localhost_ip = (mysoc.gethostbyname(host))
	print("[S]: Server IP address is  ", localhost_ip)
	csockid, addr = tss.accept()
	print ("[S]: Got a connection request from a client at", addr)

	hostname = csockid.recv(100).encode('utf-8')
	while len(hostname) != 0:
		csockid.send(lookUp(hostname).encode('utf-8'))
		hostname = csockid.recv(100).encode('utf-8')

	tss.close()

createDict()
server()
lookUp("www.rutgers.")
