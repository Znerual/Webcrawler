#requests_html needs to be installed with pip, yahoo_fin too
#lxml neeeds to be installed as well

from bs4 import BeautifulSoup as Bsoup
from yahoo_fin import stock_info as si
import requests

url = "https://in.finance.yahoo.com/most-active"


def main():

    print("hey")
    names = []
    prices = []
    changes = []
    percentChanges = []
    marketCaps = []
    totalVolumes = []
    circulatingSupplys = []

    result = requests.get(url)
    soup = Bsoup(result.content, 'html.parser')
    print("Haefd")
    for listing in soup.find_all('tr', attrs={'class': 'simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white)'}):
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Price (intraday)'}):
            prices.append(price.find('span').text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes.append(change.text)
        for percentChange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges.append(percentChange.text)
        for marketCap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps.append(marketCap.text)
        for totalVolume in listing.find_all('td', attrs={'aria-label': 'Avg vol (3-month)'}):
            totalVolumes.append(totalVolume.text)
        for circulatingSupply in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            circulatingSupplys.append(circulatingSupply.text)
    print(len(names))
    #for i in range(0, len(names)):
      #  print(float(changes[i][0:len(percentChanges[i]) - 1]))
       # print(float(percentChanges[i][0:len(percentChanges[i])-1]))

    print(si.get_day_gainers().columns) #is a pandas data frame

main()
