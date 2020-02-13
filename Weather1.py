#!/usr/bin/env python
# coding: utf-8

# In[10]:


import Speaker1
import Listener

def weather(x):
    
    y = x.split(" ")

    ind = 0
    ind2 = None

#     print(y)

    for i in y:
        if i == 'temperature' or i == 'weather':

                print('Initiating temperature search')

    if 'in' in y:

        ind = y.index('in')

    if 'on' in y:

        ind2 = y.index('on')
        
    if 'outside' in y:
        
        url = 'https://www.google.com/search?q=weather'

    elif ind == 0 and 'outside' not in y:

        msg1 = 'Please specify the place'

        Speaker1.speak(msg1)
        Place = Listener.listen()

        Place = Place.replace(' ','+')

    else:

        placelist = y[ind+1:ind2]

        Place = ''

        for i in placelist:
            Place = Place +' ' + i
            Place = Place.lstrip().replace(' ','+')

    if ind2 != None:

        datelist = y[ind2 + 1:]

        Date = ''

        for i in datelist:
            Date = Date +' ' + i
            Date = Date.lstrip().replace(' ','+')


        url = 'https://www.google.com/search?q=weather+in+'+ Place +'+on+'+ Date
        
    elif ind != 0:
        url = 'https://www.google.com/search?q=weather+in+'+ Place
        
    else:
        url = 'https://www.google.com/search?q=weather'

    from selenium import webdriver
    path="chromedriver.exe"

    import time
    import random
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome(path, options = chrome_options)
    driver.get(url)

    # assert 'Google' in driver.title

    p1 = driver.find_elements_by_xpath('//*[@id="wob_tm"]')

    for hamilton in p1:
        
        celsius = round((int(hamilton.text) - 32) * (5/9),0)        
        celsius = str(celsius)
        
        x= 'Temperature is ' + hamilton.text + ' degree Farenheit' + ' or ' + celsius + ' celsius'

        Speaker1.speak(x)


    p2 = driver.find_elements_by_xpath('//*[@id="wob_d"]/div/div[2]')

    lenn = len(p2)

    for i in p2:

        strin = i.text
        listt = strin.split('\n')

        for i in range(len(listt)-1):

            ele = listt[i].split(":")

            y = ele[0] +' is'+ ele[1]

            Speaker1.speak(y)

    driver.close()

    Date = None
    Place = None

