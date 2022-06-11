from bs4 import BeautifulSoup
import requests


url = "https://www.instagram.com/realraminfp/"
res = requests.get(url)
if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    lst = soup.find_all('script')
    print(lst)
