from bs4 import BeautifulSoup 
import requests

#Scrapes the data from the site and helps to format it
def checker(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += (str(i+1)+'\t\t' + tag.text + "\n"+ " \t\t" + tag.a.get('href') + "\n")
    return(cnt)


#Sets it off
def main():
    url = input("What is the URL that we are scanning?")
    '''html= BeautifulSoup('url','html.parser')
    print(html.findall)'''
    #cnt = checker(url)
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data,features='lxml')

    for possibleVuln in soup.find_all('input'):
        print(possibleVuln,"\n")
    
#Begins program
main()