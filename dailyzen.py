#This app grabs the text from dailyzen and prints it to the command line.
#It uses the beautifulsoup and requests libraries to achieve this.

import requests
from bs4 import BeautifulSoup, Comment
from sys import exit

def quote(r):
	soup = BeautifulSoup(r.text, from_encoding='utf-8')
	comments = soup.findAll(text=lambda text:isinstance(text, Comment))
	[comment.extract() for comment in comments]
	soup = soup.p
	print ''
	for string in soup.stripped_strings:
		string = string.replace(u'\x96','-')
		string = string.replace(u'\x97','-')
		if string[0] == '-': print '\n' + string + '\n'
		else: print string
	return

def main():
	try:
		r = requests.get('http://www.dailyzen.com/')
	except:
		response = raw_input('\nWebsite error\nRetry? (y/n): ')
		if response == 'y': main()
		else: exit(0)
	quote(r)

if __name__ == '__main__':
	main()