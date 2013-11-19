#This app grabs the text from dailyzen and prints it to the command line.
#It uses the beautifulsoup and requests libraries to achieve this.

import requests
from bs4 import BeautifulSoup, Comment
from sys import exit

def checksite(r):
	if r.status_code == 200: return True
	else: return False

def quote(r):
	soup = BeautifulSoup(r.text, from_encoding='utf-8')
	comments = soup.findAll(text=lambda text:isinstance(text, Comment))
	[comment.extract() for comment in comments]
	soup = soup.p
	print ''
	for string in soup.stripped_strings:
		string = string.replace(u'\x96','-')
#		if string[0] == '-': print '\n'
		print string + '\n'
	return

def main():
	r = requests.get('http://www.dailyzen.com/')
	if checksite(r):
		quote(r)
	else:
		print 'Website error: ' + r.status_code
		response = raw_input('Retry? (y/n): ')
		if response == 'y': main()
		else: sys.exit(0)

if __name__ == '__main__':
	main()