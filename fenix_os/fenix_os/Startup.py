#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fenix_os.Wrapper import Wrapper

"""
Class attribute :
    - Minitel minitel
    - string content

Class method :
    - Connect()
    - Disconnect()
    - GetString(char end)
    - SendString(string content)
    - SendString(string content, int line, int column)
"""

class Startup: # To get linked with the system that communicate directly with the Minitel
    
    def __init__(self): # Constructor
        self.Launch()

    def Launch(self):
        w = Wrapper()
        w.Connect()
        w.WriteString("Launched successfully")
        tmp = w.ReadString()
        print("string : {}".format(tmp))
        w.Disconnect()        
        
