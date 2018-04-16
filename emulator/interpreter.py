#!/usr/bin/python3

from __future__ import print_function

from write_characters import *

pos = 0;

def move_down_one_line(screen_list, pos):
	pos = pos - 40
	i = 0
	while (i < 40):
		del screen_list[i]
		screen_list.append(None)
		i = i + 1
	return (pos)

def interpreter(key_ch, ascii_list, screen_list, main):
		global pos
		if (pos + 1 >= len(screen_list)):
			pos = move_down_one_line(screen_list, pos)
			refresh_screen(ascii_list, screen_list, main)
		if (key_ch == "\\x08" and pos > 0):
			delete_one_space(screen_list, pos, main)
			pos = pos - 1
			screen_list[pos] = 'underscore'
			write_on_screen(ascii_list, screen_list, pos, main)
		elif (key_ch == ' '):
			delete_one_space(screen_list, pos, main)
			pos = pos + 1
			screen_list[pos] = 'underscore'
			write_on_screen(ascii_list, screen_list, pos, main)
		elif ((key_ch >= 'A' and key_ch <= 'Z') or (key_ch >= 'a' and key_ch <= 'z') or key_ch == '(' or key_ch == ')' or key_ch == '[' or key_ch == ']'):
			screen_list[pos] = key_ch
			write_on_screen(ascii_list, screen_list, pos, main)
			pos = pos + 1
			screen_list[pos] = 'underscore'
			write_on_screen(ascii_list, screen_list, pos, main)
		elif (key_ch == '\\r'):
			pos = pos + (40 - (pos % 40))
		else:
			pass
