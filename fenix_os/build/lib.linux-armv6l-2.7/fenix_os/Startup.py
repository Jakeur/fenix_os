#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fenix_os.Wrapper import Wrapper
from fenix_api.FenixTwitter import FenixTwitter

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

    w = None
    t = None
    
    def __init__(self): # Constructor
        self.Launch()

    def Launch(self):
        self.w = Wrapper()
        self.w.Connect()
        self.w.WriteLnString("Minitel launched successfully")

        self.t = FenixTwitter()
        #self.TryConnectTwitter()
        tweets = self.t.GetTweets()
        for tmp in tweets:
            self.w.WriteLnString(tmp)
            self.w.WriteLnString()
        #tmp = w.ReadString()
        #print("string : {}".format(tmp))
        
        self.w.Disconnect()

    def TryConnectTwitter(self, attempt = 1):
        if (attempt > 3):
            self.w.WriteLnString("Can't connect to Twitter API")
            return
        self.w.WriteLnString("Connecting to Twitter API. Attempt " + str(attempt))
        answer = self.t.Request()
        if (answer is None):
            self.w.WriteLnString("Status: No internet connection")
            self.TryConnectTwitter(attempt + 1)
        elif (answer.status_code != 200):
            self.w.WriteLnString("Status: " + str(answer.status_code) + ": Error")
            self.TryConnectTwitter(attempt + 1)
        else:
            self.w.WriteLnString("Status: " + str(answer.status_code) + ": Connected")
