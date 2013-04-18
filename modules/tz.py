"""
time.py - Phenny Time/Zone Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import urllib, simplejson

def tz(phenny, input):
	try:
		htmlinput  = urllib.quote(input.group(2))
		url2 = 'http://nominatim.openstreetmap.org/search?q=' + htmlinput + '&format=json'
		jsonResponse = simplejson.load(urllib.urlopen(url2))
		lati = jsonResponse[0]['lat']
		longi = jsonResponse[0]['lon']
		url3 = 'http://api.geonames.org/timezoneJSON?lat=' + lati + '&lng=' + longi + '&username=jinpark'
		jsonResponse1 = simplejson.load(urllib.urlopen(url3))
		phenny.say(jsonResponse1['time'])
	except:
		phenny.say('Something went wrong')


ud.commands = ['tz']
ud.priority = 'low'