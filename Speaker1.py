#!/usr/bin/env python
# coding: utf-8

# In[9]:


def speak(message):

    import pyttsx3
    engine = pyttsx3.init() 

    engine.say(message) 
    engine.runAndWait()
    engine.stop()

