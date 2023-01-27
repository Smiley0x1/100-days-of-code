#Creates a document that contains the top 30 stories on HackerNews
from bs4 import BeautifulSoup 
import requests
from datetime import date

#Scrapes the data from the site and helps to format it
def scrapper(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('HN Top Stories:\n'+'-'*150+'\n')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += (str(i+1)+'\t\t' + tag.text + "\n"+ " \t\t" + tag.a.get('href') + "\n")
    return(cnt)

#Writes the data to a txt
def writefile(cnt):
    with open("NewsCollection/" + str(date.today()) + ".txt", "w",encoding="utf-8") as f:
        f.write(cnt)
    
#Sets it off
def main():
    cnt = scrapper('https://news.ycombinator.com/')
    writefile(cnt)
    
#Begins program
main()