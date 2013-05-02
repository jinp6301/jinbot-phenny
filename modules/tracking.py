"""
tracking.py - Phenny Package Tracking Module
Copyright 2013, Jin Park - jinpark.net
API used from AfterShip
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
http://jinpark.net
"""

import requests

def tracking(phenny, input):
	track = input.group(2).split(', ')

	url = 'https://api.aftership.com/v2/trackings.json/'
	values = {'api_key':'d362658619a687b15e62ada6638e71d7c9c2daa7', 'tracking_number': track[0], 'courier': track[1]}

	r = requests.post(url,data = values)

	url1 = 'https://api.aftership.com/v2/trackings.json/?api_key=' + 'd362658619a687b15e62ada6638e71d7c9c2daa7' + '&tracking_number=' + track[0] + '&courier=' + track[1]

	resp = requests.get(url1)

	tracktime =  resp.json()['checkpoints'][-1]['checkpoint_time']
	trackmessage =  resp.json()['checkpoints'][-1]['message']

	phenny.reply('Time: ' + tracktime + ' ' + 'Message: ' + trackmessage)


tracking.commands = ['track']
tracking.priority = 'low'

