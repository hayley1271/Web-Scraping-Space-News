"""Web Scraping Space News

Scraping news from the https://www.space.com/news web page

Extracting the news stories and printing out the headline, author, synopsis, and date and time for each story

Examining the structure of the page to find the HTML for the articles then using requests and BeautifulSoup to explore data extraction
"""

import requests
url = 'https://www.space.com/news'
headers = {'user-agent': 'Hayley Baek, Web Scraping Space News exercise'}
request = requests.get(url, headers=headers)
request.ok # returns True
data = request.text
#print(data)

from bs4 import BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')
print(soup.prettify())

# want to print headline, author, synopsis, date, and time 
news_list = soup.find_all('div', class_='content') # returns list of each news article on the webpage
# iterating through each article in the list
for row in news_list: 
  article_name = row.find('h3', class_='article-name')
  author_name = row.find('span', class_='by-author')
  synopsis = row.find('p', class_='synopsis')

  # getting datetime and reformatting
  datetime = row.find('time')['datetime']
  datetime_list = datetime.split('T')
  # formatting day
  date = datetime_list[0].split('-')
  # formatting time
  if int(datetime_list[1][:2]) > 12:
    time = str(int(datetime_list[1][:2])-12) + datetime_list[1][2:-4] + 'PM'
  elif int(datetime_list[1][:2]) == 12:
    time = datetime_list[1][:-4] + 'PM'
  else:
    time = datetime_list[1][:-4] + 'AM'
  
  # printing all the information
  print('Headline:', article_name.get_text())
  print('Author:', author_name.get_text()[5:-1])
  print('Synopsis:',synopsis.get_text()[1:-1])
  print('Posted:',date[1]+'/'+date[2]+'/'+date[0], time)
  print('\n')
