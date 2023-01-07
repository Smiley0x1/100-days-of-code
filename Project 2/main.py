from bs4 import BeautifulSoup 
import requests

def scrapper(url):
    
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('HN Top Stories:\n'+'-'*150+'\n')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += (str(i+1)+'\t'+ tag.a.get('href') + '"\t' + tag.text + "\n")
    return(cnt)

cnt = scrapper('https://news.ycombinator.com/')


print(cnt)
'''def writefile(HTML):
    pass

def main():
    pass
    
    
main()'''