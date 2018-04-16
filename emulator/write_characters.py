#!/usr/bin/env python
# -*- coding uft-8 -*-

from Tkinter import *

rect_list = []
for i in range(0, ((40 * 25) - 1)):
	rect_list.append([i])

#write_on_screen(ascii_list, screen_list, main)
#----------------------------------------------------------------------------------------------------#
def write_8x10(ascii_list, pos, screen_list, main):
	global rect_list
	x_pos = (pos * 8 * 4) % (320 * 4)
	y_pos = int((pos / 40)) * (10 * 4)
	i = 1
	while (i < len(ascii_list)):
		rect_list[pos].append(main.create_rectangle((x_pos + (int(ascii_list[i][0]) * 4)), (y_pos + (int(ascii_list[i][1]) * 4)), (x_pos + (int(ascii_list[i][0]) * 4)) + 4, (y_pos + (int(ascii_list[i][1]) * 4)) + 4, fill="white", outline="white"))
		i = i + 1

def refresh_screen(ascii_list, screen_list, main):
	main.delete("all")
	global rect_list
	rect_list = []
	for i in range(0, ((40 * 25) - 1)):
		rect_list.append([i])
	pos = 0;
	while (pos < len(screen_list)):
		k = 0
		while (k < len(ascii_list)):
			if (ascii_list[k][0] == screen_list[pos]):
				write_8x10(ascii_list[k], pos, screen_list, main)
			k = k + 1
		pos = pos + 1

def write_on_screen(ascii_list, screen_list, pos, main):
	delete_one_space(screen_list, pos, main)
	k = 0
	while (k < len(ascii_list)):
		if (ascii_list[k][0] == screen_list[pos]):
			write_8x10(ascii_list[k], pos, screen_list, main)
		k = k + 1

def delete_one_space(screen_list, pos, main):
	global rect_list
	if (rect_list[pos] and len(rect_list[pos]) > 1):
		for i in range(1, len(rect_list[pos])):
			main.delete(rect_list[pos][i])
		for i in range(1, len(rect_list[pos])):
			del rect_list[pos][1]
#----------------------------------------------------------------------------------------------------#
