#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 16:19:40 2022

@author: sq
"""

from gtts import gTTS
import sounddevice as sd
from scipy.io.wavfile import write
import time


class Sound():
    def __init__(self):
        self.fs = 44100
        self.listen_for = 6
        self.listen_fn = 'tmp_listen.wav'
        self.speak_fn = 'tmp_speak.mp3'
        self.language = 'en'
        self.tld = 'ie'
    
    
    def listen(self):
        
        
        myrecording = sd.rec(int(self.listen_for * self.fs), channels=1)
        time.sleep(1)                           
        print('Recording. Ask Alfred your question')
        sd.wait() 
        print("Recording stopped, saving to {}.".format(self.listen_fn))
        
        write(self.listen_fn, self.fs, myrecording) 
        
        return self.listen_fn
        
    def speak(self, text):
        
        speak_obj = gTTS(text=text, lang=self.language, slow=False, tld=self.tld)
        speak_obj.save(self.speak_fn)
        
        return self.speak_fn
        
        
        

    
    
    