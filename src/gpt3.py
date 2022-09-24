#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 16:33:52 2022

@author: sq
"""

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
   

class GPT3_Q_AND_A():
    
    def __init__(self, log):
        self.chat_log = log
        self.engine = "text-davinci-002"
        self.temp = 0.7
        self.max_tokens = 2048
        self.frequency_penalty = 0.2
        self.presence_penalty = 0.2
    
        
    def get_answer(self, question):
        
        self.chat_log += '\n'+question
            
        response = openai.Completion.create(
                engine=self.engine,
                prompt=self.chat_log,
                temperature=self.temp,
                max_tokens=self.max_tokens,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
        )
    
        self.chat_log += response.choices[0].text +'\n'
        
        return response.choices[0].text