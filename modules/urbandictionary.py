"""
urbandictionary.py - Phenny Urban Dictionary Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import urllib, json
import string

def ud(phenny, input):
	try:
		htmlinput  = urllib.quote(input.group(2))
		url2 = 'http://api.urbandictionary.com/v0/define?term=' + htmlinput
		googleResponse = urllib.urlopen(url2)
		jsonResponse = json.loads(googleResponse.read())
		defin = jsonResponse['list'][0]['definition']
		phenny.say(defin)

	except:
		return


ud.commands = ['ud']
ud.priority = 'low'