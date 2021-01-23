from time import sleep
from bs4 import BeautifulSoup as bs
import collections
import requests
import re
import socket
import sys

url = "http://free-proxy.cz/en/"

""" mini-map
1) make pagination mechanism
2) get ip/port
3) save data into file
"""

"""
Shit doesn't work
"""

def myfunc():
    session = requests.Session()
    page = session.get(url)
    content = bs(page.content, 'lxml')
    print(content)


def connectThroughProxy():
    headers = """GET http://www.example.org HTTP/1.1\r\n\r\nHost: www.example.org\r\n\r\n"""


    host = "104.131.116.158" #proxy server IP
    port = 8080              #proxy server port

    try:
        s = socket.socket()
        s.connect((host,port))
        s.send(headers.encode('utf-8'))
        response = s.recv(3000)
        print (response)
        s.close()
    except socket.error as m:
       print (str(m))
       s.close()
       sys.exit(1) 

connectThroughProxy()

