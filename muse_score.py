#Suche auf Seite nach den namen der Input Felder
#username, password, _csrf

import requests
from bs4 import BeautifulSoup as soup

login_url = "https://musescore.com/user/login?destination=%2Fcas%2Flogin"
url = "https://musescore.com/hub/piano"


def main():
    print("start")
    #create a session
    session_requests = requests.session()

    #get the authenticity token
    result = session_requests.get(login_url)

    #beautifulsoup for getting the authenticy token
    result_soup = soup(result.content, 'html.parser')
    authenticity_token = result_soup.find("input", {"name": "_csrf"})['value']

    #read in the credentials
    credential_soup = soup(open("credentials.html"), 'html.parser')
    muse_score_credential_container = credential_soup.find("div", {"class":"muse_score"})
    USERNAME = muse_score_credential_container.find("input", {"name":"username"})['value']
    PASSWORD = muse_score_credential_container.find("input", {"name":"password"})['value']

    #create the payload for login
    payload = {"username": USERNAME,
               "password": PASSWORD,
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