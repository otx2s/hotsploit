#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import random
import sys
import os
from time import sleep as ts
from core.colors import *
from core.comand import *
from core import menu
from core import help
from core import logo
from core import show_modules
from modules import scanner

##################
# СДЕЛАТЬ МОДУЛИ #
##################

clear()
logo.logo()
menu.menu()

def main():
	try:
		first = BOLD+W+"hsf"+W
		first += " > "
		console = input(first)
		if console == "help":
			help.help()
			main()

		elif console == "use" or console == "use ":
			print(R+"\nFor example"+W+":"+BOLD+" use scan/scanner\n"+W)
			main()

		elif console == "banner":
			logo.logo()
			menu.menu()
			main()

		elif console == "clear" or console == "cls":
			clear()
			main()

		elif console == "show modules":
			show_modules.show_modules()
			main()

		elif console == "exit":
			print(R+"\n[*]"+W+" Exiting...\n"+W)
			ts(1)

		#MODULES

		elif console == "use scan/scanner":
			scanner.scanner()
			main()

		#SYSCOM

		else:
			print(R+"\nERROR"+W+": Wrong command => " + console + "\n")
			main()

	except(KeyboardInterrupt):
		print(R+"\n\n[*]"+W+" Exiting...\n"+W)
		ts(1)

if __name__ == '__main__':
	main()
