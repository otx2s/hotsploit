#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
from time import sleep as ts
from core import help
from core.comand import *
from core.colors import *

options = ["https://google.com or 127.0.0.1"]
m = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]

def scanner():
	try:
		first = BOLD+W+"hsf"+W
		first += W+" scan"
		first += W+"("+R+"scanner"+W+")"
		first += " > "
		opt = input(first)
		if opt[0:7] == "set url":
			url = opt[8:]
			print("IP/URL => "+url)
			options[0] = url
			options[0] = options[0].replace("https://", "")
			scanner()

		elif opt == "help":
			help.help()
			scanner()

		elif opt == "back":
			pass

		elif opt == "show options":
			print("")
			print(Y+"Options\t    Value "+W)
			print(G+"-----------\t----------------"+W)
			print("URL \t\t%s " %(options[0]))
			print("")
			scanner()

		elif opt == "run":
			url = options[0]
			if url == "http://google.com or 127.0.0.1":
				print(R+"[-]"+W+" Write IP or URL! 'set url ...'"+W)
				scanner()
			else:
				url = options[0]
				g = 0
				print(B+"\n[*]"+W+" Scanner started!"+W)
				for port in m:
					sock = socket.socket()
					sock.settimeout(0.1)
					try:
						sock.connect((url, port))

					except socket.error:
						g += 1

					else:
						sock.close
						print(G+"[+] "+W+url+": "+B+str(port)+G+" port OPENED"+W)
				print(R+"[-]"+W+" CLOSED PORTS = "+W+str(g)+W)
				print(B+"[*]"+W+" Scanner stoped!\n"+W)
				scanner()

		else:
			print(R+"\nERROR"+W+": Wrong command => " + opt + "\n")
			scanner()

	except(KeyboardInterrupt):
		print(R+"\n\n[-]"+W+" (Ctrl + C ) Detected...\n"+W)
		ts(1)
		pass
