# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:25:09 2020

@author: Aryan Tengshe
"""

from CognitioFormAnAnswer import CognitioFormAnAnswer
import speech_recognition as cognt_sr
import pyttsx3

def CognitioMain():
    
    #get refrence to the instance of pyttsx3 engine
    cognt_engine = pyttsx3.init()
    cognt_engine.setProperty("rate", 120)
    #cognt_engine.setProperty("gender", "male")
    
    #Creates a Cognt_rcgnsr Recognizer instance, 
    #which represents a collection of speech recognition settings and functionality.
    #cognt_rcgnsr = cognt_sr.Recognizer()
    #Cognt_rcgnsr.energy_threshold = 4000
   
    #LOCAL VARIABLE DECLARATION:
    #declare a variable usr_question and initialise it to null.
    usr_qstn=""
    #declare a variable answrtxt2Spch and initialise it to null.
    answrtxt2Spch=""
    #declare a variable Cognt_inAudio and initialise it to null.
    cognt_inAudio = ""    
    
    #PROGRAM STARTS
    # COGNITIO introduces.
    cognt_engine.say("Hi this is Cogneeteeyo, Welcome to the source of knowledge about rivers of Pooney.") 
   
    got_input = True
    #text to speech
    cognt_engine.say("ask a question about rivers of Pooney.")
    #to run the speech we use runAndWait()
    #All the pyttsx3.say() texts won’t be said unless the interpreter encounters runAndWait().
    cognt_engine.runAndWait()

    with cognt_sr.Microphone() as cognt_source:
        #remove all disturbing noises.
        cognt_rcgnsr = cognt_sr.Recognizer()
        cognt_rcgnsr.energy_threshold = 4000
        cognt_rcgnsr.adjust_for_ambient_noise(cognt_source, duration=3)
    
        try:
            #listen.
            cognt_inAudio =cognt_rcgnsr.listen(cognt_source,timeout=5)

        except:
            print("Listen error")
            got_input = False           

        if got_input:
            try:                
                #speech to text
                usr_qstn = cognt_rcgnsr.recognize_google(cognt_inAudio)
                #Call a program to form an answer based on keyword
                answrtxt2Spch = CognitioFormAnAnswer(usr_qstn)
                cognt_engine.say(answrtxt2Spch)
                cognt_engine.runAndWait()
            except:
                print("Speech to text Error")
   