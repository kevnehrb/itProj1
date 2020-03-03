import socket as mysoc
import sys

rsListenPort = int(sys.argv[1])
dns = []
TSHostname = ""

def createDict():
	inputFile = open("PROJI-DNSRS.txt","r")
	entries = inputFile.readlines()
	for i in entries:
		newEntry = i.split()
		if newEntry[2] == 'NS':
			TSHostname = newEntry[2]
		dns.append(newEntry)
	inputFile.close()


def printDict():
	for entry in dns:
		print(entry)


def lookUp(hostname):
	print("[S]: looking up hostname: " + hostname)
	found = False
	result = hostname
	for i in dns:
		print("[S]: comparing {} with {}".format(hostname, i[0]))
		if hostname.lower() == i[0].lower():
			print("[S]: match found")
			result = i[0] + " " + i[1] + " " + i[2]
			found = True
			break
	if not found:
		print("[S]: match not found")
		result = TSHostname + " - NS"
	return result


def server():
	try:
		rss = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
		print("[S]: RS socket created")
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

	hostname = csockid.recv(100)
	while len(hostname) != 0:
		csockid.send(lookUp(hostname))
		hostname = csockid.recv(100)

	rss.close()


createDict()
server()
