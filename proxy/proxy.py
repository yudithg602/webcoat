from bs4 import BeautifulSoup as bs
import requests
session = requests.Session()

url = "https://signup.mail.com/"

response = session.get(url)
print(session.cookies.get_dict())

print(bs(response.content, 'lxml'))


