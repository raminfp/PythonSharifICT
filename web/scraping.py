# pip install beautifulsoup4
# pip install requests
# pip install lxml
import bs4
import requests

res = requests.get("https://www.python.org/")
if res.status_code == 200:
    soup = bs4.BeautifulSoup(res.text, "lxml")
    print(soup.select("title")[0].getText())
