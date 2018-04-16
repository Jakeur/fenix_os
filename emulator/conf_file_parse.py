#!/usr/bin/python3

import sys


def get_ascii_conf_file():
	try:
		with open("ascii_file.txt", "r") as file:
			ascii_list = []
			_str = ''
			for line in file:
				if line[:1] != '#' and _str[:1] == '#':
					_list = line[:-1].split('|')
					for i in range(len(_list)):
						_list[i] = _list[i].split(',')
					_list.insert(0,_str[1:])
					ascii_list.append(_list)
				_str = line[:-1]
	except(OSError, IOError):
		print("Could not find or could not open ascii_file.conf !")
		exit(84)

	return (ascii_list)
