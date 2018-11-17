import bs4
from urllib.request import urlopen
import datetime as date

def historical_index_naver(index_cd,page_n=1,last_page=0):
    naver_index="http://finance.naver.com/sise/sise_index_day.nhn?code="+index_cd+"&page="+str(page_n)

    source = urlopen(naver_index).read()
    source = bs4.BeautifulSoup(source,'html.paser')

    dates = source.find_all('td',class_='date')
    prices = source.find_all('td',class_='number_1')

for n in range(len(dates)):

    if dates[n].text.split('.')[0].isdigit():
        this_date = dates[n].text
        this_date = date_format(this_date)

        this_close = prices[n*4].text
        this_close = this_close.replace(',','')
        this_close = float(this_close)

        historical_prices[this_date] = this_close

    if last_page==0:
        last_page = source.find('td',class_='pgRR').find('a')['href']
        last_page = last_page.split('&')[1]
        last_page = last_page.split('=')[1]
        last_page = int(last_page)

    if page_n < last_page : 
        page_n = page_n +1
        historical_index_naver(index_cd,start_table,end_date,page_n,last_page)
    return historical_prices



