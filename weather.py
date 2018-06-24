#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Written by Tomasz Skiba
#
# register at https://openweathermap.org/
# copy API key from https://home.openweathermap.org/api_keys to the 'key' variable

import json
import urllib2
import time
#import pprint

# check internet connection
try:
    urllib2.urlopen('http://216.58.215.78', timeout = 3)    #google IP
except urllib2.URLError:
    print('\nNo Internet connection\n')
    quit()


key = 'your key here'
http_response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=' + key)  # get file object from the web
json_string = http_response.read()  # open file and save data as a string
json_data = json.loads(json_string)  # convert data string to json format

sunrise = time.ctime(json_data['sys']['sunrise'])[11:19] # convert unix time to local time and extract only an hour value
sunset = time.ctime(json_data['sys']['sunset'])[11:19]

print('Current temperature for %s city is %d degrees celsius') % (str(json_data['name']), json_data['main']['temp'])
print('The sun rises at %s and sets at %s') % (sunrise, sunset)

#pprint.pprint(json_data)  # uncomment all the pprint lines to see the whole json data

