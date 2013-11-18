#This app grabs the text from dailyzen and prints it to the command line.
#It uses the beautifulsoup and requests libraries to achieve this.

import requests
from bs4 import BeautifulSoup, Comment
from sys import exit

def checksite(r):
	if r.status_code == 200: return True
	else: return False

def quote(r):
	f = open('site.html','w+')
	f.write(str(r.text))
	f.close()
	f = open('site.html','r')
	soup = BeautifulSoup(f.read())
	comments = soup.findAll(text=lambda text:isinstance(text, Comment))
	[comment.extract() for comment in comments]
	soup = soup.p
	wisdom = '\n'
	for string in soup.stripped_strings:
		if string[0] == '-': wisdom += '\n'
		wisdom += string + '\n'
	f.close()
	print wisdom
	return

# An alternative way to read a file

#	with open('site.html', 'rb') as html:
#		soup = BeautifulSoup(html.read())

#	for p in soup.find_all('p'):
#		print p.get_text()

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