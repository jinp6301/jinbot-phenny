"""
urbandictionary.py - Phenny Urban Dictionary Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import urllib, json
import string

def ud(phenny, input):
	htmlinput  = urllib.quote(input.group(2))
	url2 = 'http://api.urbandictionary.com/v0/define?term=' + htmlinput
	googleResponse = urllib.urlopen(url2)
	try:
		jsonResponse = json.loads(googleResponse.read())
		defin = jsonResponse['list'][0]['word'] + ': ' + jsonResponse['list'][0]['definition']
	except:
		defin = 'No urban dictionary definition found.'
	phenny.say(defin)


ud.commands = ['ud']
ud.priority = 'low'

def ude(phenny, input):
	htmlinput  = urllib.quote(input.group(2))
	url2 = 'http://api.urbandictionary.com/v0/define?term=' + htmlinput
	googleResponse = urllib.urlopen(url2)
	try:
		jsonResponse = json.loads(googleResponse.read())
		defin = jsonResponse['list'][0]['word'] + ': ' + jsonResponse['list'][0]['example']
	except:
		defin = 'No urban dictionary example found.'
	phenny.say(defin)


ude.commands = ['ude']
ude.priority = 'low'