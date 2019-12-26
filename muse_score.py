#Suche auf Seite nach den namen der Input Felder
#username, password, _csrf

import requests
from bs4 import BeautifulSoup as soup

USERNAME = "Laurenz27"
PASSWORT = "zk9g1fT73k9SSyDmft3N"
login_url = "https://musescore.com/user/login?destination=%2Fcas%2Flogin"
url = "https://musescore.com/hub/piano"


def main():
    print("start")
    #login and get authentification
    session_requests = requests.session()

    #get the authenticity token
    result = session_requests.get(login_url)

    #xtree lxml
    #tree = html.fromstring(result.text)
    #authenticity_token = list(set(tree.xpath("//input[@name='_csrf']/@value")))[0]

    #beautifulsoup
    result_soup = soup(result.content, 'html.parser')
    authenticity_token = result_soup.find("input", {"name": "_csrf"})['value']
    payload = {"username": USERNAME,
               "password": PASSWORT,
               "_csrf": authenticity_token}

    #log in
    result = session_requests.post(login_url,
                                   data = payload,
                                   headers = dict(referer = login_url))
    if result.status_code != 200:
        print("Failure at login")
        return -1
    #proceed to main page and scrape

    result = session_requests.get(url,headers = dict(referer = url))
    result_soup = soup(result.content, 'html.parser')
    titles_container = result_soup.find_all("h2","score-info__title")
    #print(result_soup)
    for titel in titles_container:
        print(titel.a.text)

main()