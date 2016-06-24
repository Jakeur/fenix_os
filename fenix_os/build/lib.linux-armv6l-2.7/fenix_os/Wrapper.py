#!/usr/bin/env python
# -*- coding: utf-8 -*-

from minitel.Minitel import Minitel
from minitel.Sequence import Sequence
from minitel.constantes import (ENVOI, RETOUR)

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

class Wrapper: # To get linked with the system that communicate directly with the Minitel
    minitel = None
    
    def __init__(self): # Constructor
        self = self
        
    def Connect(self):  
        self.minitel = Minitel()
        if (self.minitel.deviner_vitesse() == -1):
            if (self.minitel.definir_vitesse(300) == False):
                return (1)
        self.minitel.identifier()
        self.minitel.definir_mode("VIDEOTEX")
        print("{} - {}".format(self.minitel.capacite['nom'], self.minitel.capacite['vitesse']))
        self.minitel.efface()
        self.minitel.debut_ligne()

    def ReadString(self, end = ENVOI):
        content = ""

        while True:
            received = self.minitel.recevoir_sequence(True, None)
            if (received.valeurs == end):
                content += '\0'
                break;
            content += chr(received.valeurs[0])
        return content

    def WriteString(self, text = "default"):
        nb_column = 40
        nb_line = 24
        if (self.minitel.capacite['80colonnes'] == True):
            if (self.minitel.mode == 'MIXTE'):
                nb_column = 80
        text = text[0:nb_column * nb_line]
        s_send = Sequence()
        s_send.ajoute(text)
        self.minitel.envoyer(s_send)

    def WriteLnString(self, text = ""):
        nb_column = 40
        nb_line = 24
        if (self.minitel.capacite['80colonnes'] == True):
            if (self.minitel.mode == 'MIXTE'):
                nb_column = 80
        space_to_add = nb_column - (len(text) % nb_column)
        for i in range(space_to_add):
            text += " "
        text = text[0:nb_column * nb_line]
        s_send = Sequence()
        s_send.ajoute(text)
        self.minitel.envoyer(s_send)

    def GetMinitel(self):
        return (self.minitel)

    def Disconnect(self):
        self.minitel.close()
