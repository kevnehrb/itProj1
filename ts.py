import socket as mysoc

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
lookUp("www.rutgers.")
