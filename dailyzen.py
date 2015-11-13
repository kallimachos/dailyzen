# This app grabs the text from dailyzen and prints it to the command line.
# It uses the beautifulsoup and requests libraries to achieve this.

import requests
from bs4 import BeautifulSoup
from sys import exit


def quote(r):
    soup = BeautifulSoup(r.text, "lxml", from_encoding='utf-8')
    print("\n" + soup.blockquote.get_text().strip())
    print("\n" + soup.cite.get_text().strip() + "\n")
    return


def main():
    try:
        r = requests.get('http://www.dailyzen.com/')
    except:
        response = input('\nWebsite error\nRetry? (y/n): ')
        if response == 'y':
            main()
        else:
            exit(0)
    quote(r)

if __name__ == '__main__':
    main()
