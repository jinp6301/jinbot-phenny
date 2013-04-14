
def rottentomatoes(phenny, input):
	try:
		rt1 = RT().search(input.group(2))
		rttitle = rt1[0]['title']
		rtcscore = rt1[0]['ratings']['critics_score']
		rtascore = rt1[0]['ratings']['audience_score']
		try:
			rtcconsensus = rt1[0]['critics_consensus']
		except:
			rtcconsensus = 'No consensus yet.'
		phenny.reply("\x02" + rttitle + "\x02" + ' has a critics rating of ' + str(rtcscore) + ' and has an audience rating of ' + str(rtascore) + '. The critics consensus is: ' + rtcconsensus )
	except:
	 	phenny.reply('No movie found')

rottentomatoes.commands = ['rt']
rottentomatoes.priority = 'low'