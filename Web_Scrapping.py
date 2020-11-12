import requests
import bs4

result = requests.get("http://www.example.com")
type(result) # output: <class 'requests.models.Response'>
result.text

soup = bs4.BeautifulSoup(result.text,"lxml") #beautiful soup uses the lxml package

print(soup.select("title")[0].getText()) # output: Example Domain


