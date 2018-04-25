#!/usr/bin/python3

import sys

class FileParsing:
	filename = ""

	def __init__(self):
		self.filename = "ascii_file.txt"
	
	def ParseAsciiList(self):
		try:
			with open(self.filename, "r") as file:
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
			print("Could not find or could not open " + self.filename + " !")
			exit(84)
		return (ascii_list)
