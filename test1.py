import bs4
from urllib.request import urlopen
import datetime as dt

index_cd = "KPI200"
page_n=1
naver_index="http://finance.naver.com/sise/sise_index_day.nhn?code="+index_cd+"&page="+str(page_n)

source=urlopen(naver_index).read()
#print(source)

source2=bs4.BeautifulSoup(source,"html.parser") ##not lxml
#print(source2.prettify())

td=source2.find_all("td")
print(len(td))

d=source2.find_all("td",class_="date")[0].text
print(d)

def date_format(d):
    d=str(d).replace("-",".")
    yyyy = int(d.split('.')[0])
    mm = int(d.split('.')[1])
    dd = int(d.split('.')[2])

    this_date = dt.date(yyyy,mm,dd)
    return this_date
    

this_close = source2.find_all('tr')[2].find_all('td')[1].text
this_close = this_close.replace(',','')
this_close = float(this_close)
print(this_close)