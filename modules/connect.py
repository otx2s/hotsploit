#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def connect():
	try:
		first = BOLD+W+"hsf"+W
		first += W+" scan"
		first += W+"("+R+"connect"+W+")"
		first += " > "
		opt = input(first)