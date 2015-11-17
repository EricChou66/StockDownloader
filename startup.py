'''
Created on 2015/8/22
@author: Eric
'''
import csv
import os.path
import download
from download import download_table
#This function is to compute YoY
def YoY(val1,val2):
    return (round(((val1)/(val2)-1),2)*100)
#This function is to compute Gross Margin Grwoth
def GmG(val1,val2):
    return (round(((val1)/(val2)-1),4)*100)
#This function is to decide download which file
def download_quarter(s,y):
    if s==2:
        download_table(y,s,"cq.csv")
        download_table(y,(s-1),"lq.csv")
        download_table(y-1,(s+2),"tqbq.csv")
    elif s==1:
        download_table(y,s,"cq.csv")
        download_table(y-1,(s+3),"lq.csv")
        download_table(y-1,(s+2),"tqbq.csv")
    else:
        download_table(y,s,"cq.csv")
        download_table(y,(s-1),"lq.csv")
        download_table(y,(s-2),"tqbq.csv")
    return
#This function is to remove the data xml
def removexml():
    os.remove("cq.csv")
    os.remove("lq.csv")
    os.remove("tqbq.csv")
    return

year = input("Please input the year: ")
season = input("Please input the quarter: ")
print('Make sure that you want to calculate year: ',year,' season: ',season)
s = int(season)
y = int(year)
download_quarter(s,y)
with open("cq.csv",'r') as csvfile1, open("lq.csv",'r') as csvfile2, open("tqbq.csv",'r') as csvfile3, open("output.csv",'w',newline='') as outfile:
    wf = csv.writer(outfile)
    row1 = list(csv.DictReader(csvfile1))
    row2 = list(csv.DictReader(csvfile2))
    row3 = list(csv.DictReader(csvfile3))
    wf.writerow(["公司代號","公司名稱","營收成長率(%)","上季營收成長率(%)","毛利成長率(%)","上季毛利成長率(%)"])
    for i in range(len(row1)):
        yoy_cq = "--"
        gmg_cq = "--"
        yoy_lq = "--"
        gmg_lq = "--"
        for j in range(len(row2)):
            if int(row1[i]['公司代號'])==int(row2[j]['公司代號']):
                yoy_cq = YoY(float(row1[i]['營業收入']),float(row2[j]['營業收入']))
                gmg_cq = GmG((float(row1[i]['營業毛利（毛損）淨額'])/float(row1[i]['營業收入'])),(float(row2[j]['營業毛利（毛損）淨額'])/float(row2[j]['營業收入'])))
                yoy_lq = "--"
                gmg_lq = "--"
                for k in range(len(row3)):
                    if int(row2[j]['公司代號'])==int(row3[k]['公司代號']):
                        yoy_lq = YoY(float(row2[j]['營業收入']),float(row3[k]['營業收入']))
                        gmg_lq = GmG((float(row2[j]['營業毛利（毛損）淨額'])/float(row2[j]['營業收入'])),(float(row3[k]['營業毛利（毛損）淨額'])/float(row3[k]['營業收入'])))
                        break
                break
        wf.writerow([row1[i]['公司代號'],row1[i]['公司名稱'],yoy_cq,yoy_lq,gmg_cq,gmg_lq])

removexml()
print("Your result file is generated as output.csv...")
print("Press enter to finish")
input()