#!/bin/python3
# This app grabs the text from dailyzen and prints it to the command line.

import requests
from bs4 import BeautifulSoup

URL = 'http://www.dailyzen.com/'


def main(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        print('\n' + soup.blockquote.get_text().strip())
        print('\n' + soup.cite.get_text().strip() + '\n')
        return(0)
    except Exception as e:
        print('An error occured:\n' + str(e))
        return(1)

if __name__ == '__main__':
    main(URL)
