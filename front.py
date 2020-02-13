#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Speaker1
import Listener
import Listener2
import Weather1
import Songs
import word

resp = True

#ini = Listener.listen()
ini = Listener2.listen()
print(ini)

if 'andy' in ini or 'brandy' in ini:
# if ini == 'hey Brandy':

    msg0 = 'Hey! How can I help You today?'

    Speaker1.speak(msg0)

    while resp == True:
        
        #x = Listener.listen()
        x = Listener2.listen()
        x = x.lower()
        
        if 'temperature' in x or 'weather' in x :
        
            Weather1.weather(x)
            
        elif 'open world' in x or 'open word' in x:
            
            word.word()
            
        elif 'play' in x:
            
            Songs.play(x)
        
        Speaker1.speak('do you want further assistance?')
        
        #more = Listener.listen()
        more = Listener2.listen()
        more = more.lower()
        
        if more == 'yes':
            
            resp = True
            
            Speaker1.speak('Okay! what else can I do for you?')
               
        else:
            
            resp = False
            
            Speaker1.speak('Okay! Have a good day.')


#  <font color = 'blue'> **Artificial Intelligence**<font>
#     
# <font color = 'blue'> **Brandy** </font>
#     
# 
# <font color = 'blue'> Features : </font>
#     
# <font color = 'blue'> Weather reporting </font>
#     
# <font color = 'blue'> Music Playback </font>
#     
# <font color = 'blue'> Document writing </font>

#  

#  

#  

#  

#  

#  

#  
#  
#  
#  

#  

#  

#  

#  
