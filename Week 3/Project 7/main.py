from bs4 import BeautifulSoup 
import requests

def main():
    url = input("What is the URL that we are scanning?")
    req  = requests.get(url)
    data = req.text
    soup = BeautifulSoup(data,features='lxml')

    for possibleVuln in soup.find_all('input'):
        print(possibleVuln,"\n")
    
main()