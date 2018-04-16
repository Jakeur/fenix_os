#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

#import functions from other files
from conf_file_parse import *
from write_characters import *
from interpreter import *

#Window + canvas
#----------------------------------------------------------------------------------------------------#
window = Tk()
#canvas
main = Canvas(window, width=320 * 4, height=250 * 4, background="black")
#----------------------------------------------------------------------------------------------------#

#two main lists
#----------------------------------------------------------------------------------------------------#
ascii_list = get_ascii_conf_file()
screen_list = [None] * (40 * 25)
#----------------------------------------------------------------------------------------------------#

text = "In 1978 France Télécom, the country's PTT, began designing the Minitel network. By distributing terminals that could access a nationwide electronic directory of telephone and address information, it hoped to increase use of the country's 23 million phone lines, and reduce the costs of printing printed phone books and employing directory assistance personnel.[4] Millions of terminals were lent for free to telephone subscribers, resulting in a high penetration rate among businesses and the public. In exchange for the terminal, the possessors of Minitel would not be given free \"white page\" printed directories (alphabetical list of residents and firms), but only the yellow pages (classified commercial listings, with advertisements); the white pages were accessible for free on Minitel, and they could be searched by a reasonably intelligent search engine; much faster than flipping through a paper directory.\nA trial with 1,500 residential telephone customers began in Ille-et-Vilai"

def key(event):
	global ascii_list
	global screen_list
	print("Keycode : " + str(event.keycode) + " State : " + str(event.state))
	ch = repr(event.char)[1:-1]
	print(ch)
	interpreter(ch, ascii_list, screen_list, main)

def callback(event):
	# print("clickde at :  x = " + str(event.x) + " y = " + str(event.y))
	main.focus_set()

main.bind("<Key>", key)
main.bind("<Button-1>", callback)
main.pack()

window.mainloop()
