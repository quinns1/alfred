#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 16:10:44 2022

@author: sq

TODO:
    1. Speech exit condition
    2. Make faster duh
    3. Create better prompt file with 
"""

from datetime import datetime
import time
import vlc
import whisper      


from audio import Sound
from gpt3 import GPT3_Q_AND_A




def main(prompt_file = 'prompt.txt'):
       
    with open(prompt_file) as f:
        prompt = f.read()

    sound_ctrl = Sound()
    language_model = GPT3_Q_AND_A(prompt)
    whisper_model = whisper.load_model("tiny")
    
    try:
        while True:
        
            'Step 1: Listen for question'
            recording_fn = sound_ctrl.listen()
        
        
            'Step 2: Convert question to english'
        
            audio = whisper.load_audio(recording_fn)
            audio = whisper.pad_or_trim(audio)
            mel = whisper.log_mel_spectrogram(audio).to(whisper_model.device)
            dec_options = whisper.DecodingOptions()
            question = whisper.decode(whisper_model, mel, dec_options)    
            question = 'Shane: ' + question.text
        
            'Step 3: Ask Alfred question'
            answer = language_model.get_answer(question)
            parsed_answer = answer.split(':')[1]
        
            'Step 4: Speak answer back & append log' 
            answer_rec_fn = sound_ctrl.speak(parsed_answer)
        
            p = vlc.MediaPlayer(answer_rec_fn)
            p.play()
            time.sleep(5)    


    except KeyboardInterrupt:
        time_stamp = datetime.now().strftime("%m%d%Y%H%M%S")
        chat_log = 'alfred_chat_log_'+time_stamp+'.txt'
        with open(chat_log, 'w+') as f:
            f.write(language_model.chat_log)


if __name__ == '__main__':
    main()
    
    
    

    
    
    
    
