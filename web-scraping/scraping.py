#Fonte: https://imasters.com.br/back-end/como-fazer-web-scraping-com-python
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://g1.globo.com/sp/sao-paulo/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    if res.title is None:
        print("Tag not found")
    else:
        print(res.title)
        tags = res.findAll("h3", {"class": "post-title"})
        for tag in tags:
            print(tag.getText())