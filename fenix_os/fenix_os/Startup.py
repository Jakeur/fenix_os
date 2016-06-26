#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fenix dependencies
from fenix_os.Wrapper import Wrapper
from fenix_api.FenixTwitter import FenixTwitter

# System dependencies
from multiprocessing import Process
from threading import Thread, Condition
import threading
import time
import sys

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
    thread_twitter_get = None
    thread_twitter_send = None
    new_tweet = False # Used to refresh stream with the new tweet that the user entered
    lock_input = False
    writing_tweet = False
    
    def __init__(self): # Constructor
        self.Launch()

    def TwitterThreadGetStream(self, cond):
        while True:
            print("loading all tweets")
            self.lock_input = True
            tweets = self.t.GetTweets()
            self.lock_input = False
            self.w.ClearScreen()
            self.WriteHeader()
            i = 0;
            for tmp in tweets:

                # Lock this Thread() while writing tweet
                cond.acquire()
                if self.writing_tweet == True:
                    cond.wait()
                    i = 0
                cond.release()

                # Sending a new tweet to stream
                if self.new_tweet:
                    self.new_tweet = False
                    self.w.ClearScreen()
                    self.WriteHeader()
                    self.w.WriteLnString("Refreshing Twitter stream...")
                    break

                # Write tweet stream
                self.w.WriteLnString(tmp)
                self.w.WriteLnString()
                self.w.WriteLnString()
                i += 1
                if i >= 15: # No more than 15 latest tweets displayed
                    time.sleep(10)                
                    break        
                if i % 3 == 0: # 3 tweets per page
                    time.sleep(10)
                    if self.writing_tweet == True:
                        continue
                    self.w.ClearScreen()
                    self.WriteHeader()

    def TwitterThreadSendMessage(self, cond):
        msg = str()
        while (True):
            # Wait for any key input
            self.w.WaitForAnyInput()
            if self.lock_input == True:
                continue
            print("clicked")

            # Pause Twitter Stream to write message
            cond.acquire()
            self.writing_tweet = True
            print("you can write now")

            # Display instructions
            self.w.ClearScreen()
            self.WriteHeader()
            self.w.WriteLnString("1. Write something (140 characters max)")
            self.w.WriteLnString("2. Press 'Envoi' button")
            self.w.WriteLnString("3. There is no 3. step")            
            self.w.WriteLnString()
            self.w.WriteString("#VivaTech ")

            # Get user tweet
            self.w.DisplayCursor(True)
            msg = self.w.ReadString()
            if msg is not None:
                msg = "#VivaTech " + msg
                #answer = self.t.SendTweet(msg) # Send Tweet
                time.sleep(2)
                #print(answer.status_code)
                print("msg: " + msg)

            # Resume Twitter Stream
            self.new_tweet = True
            self.w.DisplayCursor(False)
            cond.notify()
            self.writing_tweet = False
            print("end input")
            cond.release()
            
    def Launch(self): # Pour le moment tout ce fait ici, c'est un peu sale mais je vais tout nettoyer après le salon

        # Init wrapper and Twitter API connection
        self.w = Wrapper()
        self.w.Connect()
        self.w.DisplayCursor(False)
        self.w.WriteLnString(self.w.GetModel()+ " launched successfully")
        self.t = FenixTwitter()
        #self.TryConnectTwitter()

        # Init suspend Twitter stream during message writing
        cond = Condition()

        # Init and launch stream and writing threads
        self.thread_twitter_get = Thread(None, self.TwitterThreadGetStream, None, (cond,))
        self.thread_twitter_send = Thread(None, self.TwitterThreadSendMessage, None, (cond,))
        self.thread_twitter_get.start()
        self.thread_twitter_send.start()

        # Properly disconnect and close the Minitel
        self.thread_twitter_get.join()
        self.thread_twitter_send.join()
        self.w.Disconnect()
        print("disconnected")

    def WriteHeader(self):
        self.w.WriteLnString("Fenix OS v0.2 - #VivaTech Twitter stream")
        self.w.WriteLnString("----------------------------------------")
        self.w.WriteLnString()

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
