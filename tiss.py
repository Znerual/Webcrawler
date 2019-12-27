import requests
from bs4 import BeautifulSoup as soup

login_url = "https://oase.it.tuwien.ac.at/AuthServ.authenticate?app=76"
data_url = "https://tiss.tuwien.ac.at/education/favorites.xhtml"
data_url2 = "https://tiss.tuwien.ac.at/main/student"

def main():
    #input as name for username and pw for password

    #start a session
    session_requests = requests.Session()


    #get cookie for authentification
    result = session_requests.get(login_url)
    print(session_requests.cookies.get_dict())
    #extract authentification details
    result_soup = soup(result.content,'html.parser')
    #print(str(result_soup))
    f = open("tissScrapeResult.html", "w", encoding='utf-8')
    f.write(str(result_soup))
    f.close()

    #i cant find the authentification cookie, lets try without
    # read in the credentials
    credential_soup = soup(open("credentials.html"), 'html.parser')
    credential_container = credential_soup.find("div", {"class": "tiss"})
    USERNAME = credential_container.find("input", {"name": "username"})['value']
    PASSWORD = credential_container.find("input", {"name": "password"})['value']
    payload = {"name" : USERNAME,
               "pw": PASSWORD,
               "totp":"",
               "app":76}

    #send the post request
    result = session_requests.post(login_url,data=payload, headers=dict(referer=login_url))

    print(session_requests.cookies.get_dict())

    if result.status_code == 200:
        print("Hurray! We did it")

    #result = session_requests.get(data_url, headers = dict(referer = data_url))
    result = session_requests.get(login_url, headers = dict(referer = login_url))
    result_soup = soup(result.content,'html.parser')
    f = open("tissScrape.html", "w", encoding='utf-8')
    f.write(str(result_soup))
    f.close()
main()