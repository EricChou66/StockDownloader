'''
Created on 2015/8/22
@author: Eric Chou
'''
import requests
import csv
from bs4 import BeautifulSoup

def download_table(y,s,filename):
    #convert season
    season = '0'
    season += str(s)
    year = str(y)
    url = 'http://mops.twse.com.tw/mops/web/ajax_t163sb04'    
    head = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9;*/*;q=0.8","Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3","Accept-Encoding":"gzip, deflate","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Referer": "http://mops.twse.com.tw/mops/web/t163sb04"}
    par = {'encodeURIComponent':'1','step':'1','firstin':'1','off':'1','TYPEK':'sii','year':year,'season':season}
    sess = requests.Session()
    res = sess.post(url,headers = head,data = par)

    #using beautifulsoup
    f = open(filename,'w',newline='')
    csvfile = csv.writer(f)
    soup = BeautifulSoup(res.content)
    table1 = soup.find_all("table",class_="hasBorder")[2]
    for tr in table1.find_all('tr'):
        ths = tr.find_all('th')
        names = [elem.text for elem in ths]
        if not(names == []):
            csvfile.writerow(names)
        tds = tr.find_all('td')
        records = []
        for elem in tds:
            strr = elem.text
            if (strr.find(',')==-1):
                records.append(strr)
            else:
                fl = strr.replace(',','')
                records.append(round(float(fl),2))   
        if not(records == []):
            csvfile.writerow(records)   
    f.close()
    return