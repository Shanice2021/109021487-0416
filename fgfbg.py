import requests
import sys
from bs4 import BeautifulSoup
url = 'https://search.books.com.tw/search/query/key/{0}/cat/all'

def A(url,keyword):
    url = url.format(keyword)
    return url

def B(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }

    return requests.get(url,headers=headers,verify=False)

def C(r):
    if r.status_code == requests.codes.ok:
        # r.encoding = 'utf-8'
        r.encoding = r.apparent_encoding
        soup =BeautifulSoup(r.text,'lxml')
        return soup
def D(url):
    booklist = []
#    print('retrive data form Int...')
    soup = C(B(url))
#    print(soup)
    return soup

if __name__ == '__main__':
    if len(sys.argv)>1:
        url = A(url,sys.argv[1])
        r = B(url)
        soup =BeautifulSoup(r.text,'lxml')
        # print(soup)
        booklist = D(url)
        bb = soup.find_all('ul')
        # for i in bb:
        print(bb)
