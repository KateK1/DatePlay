from datetime import datetime, date
from calendar import month_name
from bs4 import BeautifulSoup
from urllib import request
import random
from function import u_to_g

# проверка даты
print('Type date in yy/m/d format')
y, m, d = map(int, input().split('/'))
now_date = date(y, m, d)

calend = input('Type calendar: "g" for Gregorian, "u" for Ulian')
#lang = input('Type language en or rus')

if calend == 'g':
    now_date = now_date
elif calend == 'u':
    now_date = u_to_g(now_date)

if now_date > (datetime.today().date()):
    print('too far, boy, try another year')
# break

month = month_name[m]

URL = 'https://en.wikipedia.org/wiki/' + str(month) + '_' + str(d)

#print(URL)
req = request.urlopen(URL)
f = req.read()
soup = BeautifulSoup(f, features='html.parser')

date_pool = {}
listlist = []
for li in soup.find_all('li'):
    mystring = li.text
    if ' – ' in mystring:
        [year, event] = mystring.split(' – ')
        if str(y) == str(year):
            if '(d.' in event:
                event = event.split('(')[0] + 'was born'
            elif '(b.' in event:
                event = event.split('(')[0] + 'had died'
            listlist.append(event)

'''show = input('show all or show one random event? print "all" or "one":')
if show == 'all':
    show_all = True
elif show == 'one':
    show_one_rand = False'''
show_all = False
show_one_rand = True

if show_all:
    print(*listlist, sep='\n')
elif show_one_rand:
    for n in range(len(listlist)):
        date_pool[n] = listlist[n]
    random_number = random.randint(0, len(listlist))
    print(date_pool[random_number])

# печатать ответы по одному после энтера

