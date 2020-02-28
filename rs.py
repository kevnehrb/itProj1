import socket as mysoc

dns = []

def createDict():
	inputFile = open("PROJI-DNSTS.txt","r")
	entries = inputFile.readlines()
	for i in entries:
		newEntry = i.split()
		dns.append(newEntry)
	inputFile.close()

def lookUp(hostname):
	found = False
	for i in dns:
		for j in i:
			if hostname.lower() == j.lower():
				found = True
	if found:
		print("its in there")
	else:
		print("doo doo feces")
