#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pynput.mouse import Button, Controller as Controller_click
mouse = Controller_click()

from pynput.keyboard import Key, Controller as Controller_keys
keyboard = Controller_keys()

import time
import Listener2
import Speaker1
    
def word():
    mouse.position = (31,1057)
    mouse.click(Button.left)
    time.sleep(1)
    keyboard.type('word')
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(3)
    mouse.position = (342,242)
    mouse.click(Button.left)
    
    Speaker1.speak('What would be the name of the file')
    file_name = Listener2.listen()

    jetta = True
    while jetta ==True:

        x = Listener2.listen()
        if '.' in x:
            x = '. '
        
        if 'comma sign' in x:

            x = x.replace('comma sign',', ')

        if 'question sign' in x:

            x = x.replace('question sign','? ')

        if 'plus sign' in x:

            x = x.replace('plus sign','+')

        if 'minus sign' in x:

            x = x.replace('minus sign','-')

        if 'equal sign' in x:

            x = x.replace('equal sign','=')
            
        if 'next line' in x:

            keyboard.press(Key.enter)
            x = ''
            
        if 'spacebar' in x:

            keyboard.press(Key.space)
            x = ''
        
        if 'erase' in x:

            keyboard.press(Key.backspace)
            x = ''

        if 'close word' in x:
            
            x = ''
            
            with keyboard.pressed(Key.alt_l):
                keyboard.press(Key.f4)
                
            time.sleep(3)
            
            keyboard.type(file_name)
            
            time.sleep(2)
            
            keyboard.press(Key.enter)

            jetta = False

        keyboard.type(x)

    print('done')

