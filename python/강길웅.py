from bs4 import BeautifulSoup as bs
import urllib.request as req

url = 'http://quotes.toscrape.com/'
html = req.urlopen(url)

soup = bs(html.read(),'html.parser')
span = soup.find_all('span',{'class':"text"})

for i in span:
    print(i.text)