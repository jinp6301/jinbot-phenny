
def inp(phenny, input):
	phenny.say(input.group(2).split(', ')[1])



inp.commands = ['inp']
inp.priority = 'low'
