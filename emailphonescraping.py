'''
a Python Script to scrape websites for
email addresses and US phone numbers

Author: Yannick Le Roux

http://github.com/YannickLeRoux
'''

from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

f = urlopen('http://www.bc.edu/a-z/directories/contact/quicknos.html')

s = BeautifulSoup(f, 'html.parser')
s = s.get_text()

phone = re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",s)
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",s)

if len(phone) == 0:
    print ("Sorry, no phone number found.")

    print('------------')
    print ()
else :
    count = 1
    for item in phone:
        print ( count, ' phone number(s) found : ',item )
        count += 1

print('------------')
print()

if len(emails) == 0:
    print("Sorry, no email address found.")
    print('------------')
    print()
else:
    count = 1
    for item in emails:
        print(count, ' email address(es) found : ', item)
        count += 1
