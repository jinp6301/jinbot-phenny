
def inp(phenny, input):
	hi, hello, hey = input.groups()
	phenny.say(hi)
	phenny.say(hello)
	phenny.say(hey)


inp.commands = ['inp']
inp.priority = 'low'
