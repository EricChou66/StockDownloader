'''
Created on 2015/8/22
@author: Eric Chou
'''

import csv
import os
from download import download_table
from datetime import date

#This function is to compute YoY(Year-On-Year percentage) and GmG(Gross Margin Growth percentage)
def Calculate(val1,val2):
    if val1>10000000000 or val1<-10000000000 or val2>10000000000 or val2<-10000000000 or val2==0:
        return 'error'
    return format((((val1)/(val2)-1)*100),'.2f')

#This function is to decide download which file
def download_quarter(quarter,year):
    #The maximum input of year is current year 
    current_year = date.today().year - 1911
    if year>current_year or year<102:
        print('Wrong year input,The year is using ROC calendar(or AD minus 1991)\n')
        return False
    if quarter>4 or quarter<=0 :
        print('Wrong quarter input,The quarter is in the range 1-4\n')
        return False
    if quarter==2 and year>=102:
        if(not download_table(year,quarter,"cq.csv")):
            print("Can't find data of",year,"Q",quarter,'\n')
            return False
        if(not download_table(year,(quarter-1),"lq.csv")):
            print("Can't find data of",year,"Q",quarter,'\n')
            return False
        if(not download_table(year-1,(quarter+2),"tqbq.csv")):
            print("Can't find data of",year,"Q",quarter,'\n')
            return False
    elif quarter==1 and year>=102:
        if(not download_table(year,quarter,"cq.csv")):
            print("Can't find data of",year,"Q",quarter,'\n')
            return False
        if(not download_table(year-1,(quarter+3),"lq.csv")):
            print("Can't find data of",year,"Q",quarter,'\n')
            return False
        if(not download_table(year-1,(quarter+2),"tqbq.csv")):
            print("Can't find data of",year,"Q",quarter,'\n')
            return False
    else:
        if(not download_table(year,quarter,"cq.csv")):
            print("Can't find data of",year,"Q",quarter,'\n')
            return False
        if(not download_table(year,(quarter-1),"lq.csv")):
            print("Can't find data of",year,"Q",quarter,'\n')
            return False
        if(not download_table(year,(quarter-2),"tqbq.csv")):
            print("Can't find data of",year,"Q",quarter,'\n')
            return False
    return True
#This function is to remove the data xml
def removexml():
    if os.path.isfile("cq.csv"):
        os.remove("cq.csv")
    if os.path.isfile("lq.csv"):
        os.remove("lq.csv")
    if os.path.isfile("tqbq.csv"):
        os.remove("tqbq.csv")
    return

if __name__ == '__main__':
    year = input("Please input the year: ")
    quarter = input("Please input the quarter: ")
    while(not download_quarter(int(quarter),int(year))):
        year = input("Please input the year: ")
        quarter = input("Please input the quarter: ")
    with open("cq.csv",'r') as csvfile1, open("lq.csv",'r') as csvfile2, open("tqbq.csv",'r') as csvfile3, open("output.csv",'w',newline='') as outfile:
        wf = csv.writer(outfile)
        row1 = list(csv.DictReader(csvfile1))
        row2 = list(csv.DictReader(csvfile2))
        row3 = list(csv.DictReader(csvfile3))
        wf.writerow(["公司代號","公司名稱","營收成長率(%)","上季營收成長率(%)","毛利成長率(%)","上季毛利成長率(%)"])
        for i in range(len(row1)):
            yoy_cq, gmg_cq, yoy_lq, gmg_lq = "--", "--", "--", "--"
            for j in range(len(row2)):
                if int(row1[i]['公司代號'])==int(row2[j]['公司代號']):
                    yoy_cq = Calculate(float(row1[i]['營業收入']),float(row2[j]['營業收入']))
                    gmg_cq = Calculate((float(row1[i]['營業毛利（毛損）淨額'])/float(row1[i]['營業收入'])),(float(row2[j]['營業毛利（毛損）淨額'])/float(row2[j]['營業收入'])))
                    yoy_lq,gmg_lq = "--", "--"
                    for k in range(len(row3)):
                        if int(row2[j]['公司代號'])==int(row3[k]['公司代號']):
                            yoy_lq = Calculate(float(row2[j]['營業收入']),float(row3[k]['營業收入']))
                            gmg_lq = Calculate((float(row2[j]['營業毛利（毛損）淨額'])/float(row2[j]['營業收入'])),(float(row3[k]['營業毛利（毛損）淨額'])/float(row3[k]['營業收入'])))
                            break
                    break
            wf.writerow([row1[i]['公司代號'],row1[i]['公司名稱'],yoy_cq+'%',yoy_lq+'%',gmg_cq+'%',gmg_lq+'%'])
    removexml()
    print("Your result file is generated as output.csv...")
    print("Press enter to finish")
    input()