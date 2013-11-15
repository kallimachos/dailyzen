#This app grabs the text from dailyzen and prints it to the command line.
#It uses the beautifulsoup and requests modules to achieve this.

import requests
from bs4 import BeautifulSoup
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
	wisdom = soup.p.get_text()
	f.close()
	print '\n' + wisdom
	return

# I should be able to strip_tags the comment 'Add Author for Quote'

#an alternative quote(r)

#	with open('site.html', 'rb') as html:
#		soup = BeautifulSoup(html.read())

#	for td in soup.find_all('td'):
#		print td.get_text()

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