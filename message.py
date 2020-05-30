'''
import random

import requests
from bs4 import BeautifulSoup
# 得到所有地方航班及链接
def getAllFlights():
        flights = {}   # {'安庆航班': 'https://flights.ctrip.com/schedule/aqg..html', ...}
        url = 'https://flights.ctrip.com/schedule'
        headers = {
            'user-agent':random.choice(UserAgentq2s),
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'upgrade-insecure-requests':'1'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        letter_list = soup.find( attrs={'class':'letter_list'} ).find_all('li')
        for li in letter_list:
            for a in li.find_all('a'):
                flights[a.get_text()] = url + a['href'][9:]
        return flights

CREATE TABLE F_S(
                  航班号 CHAR(8) NOT NULL,
                  起点 VARCHAR(15),
                  终点 VARCHAR(15),
                  日期 DATETIME(6) NOT NULL,
                  起飞时刻 CHAR(6),
                  到达时刻 CHAR(6),
                  剩余座位数 INT(4),
                  票价 FLOAT(8),
                  折扣票价 FLOAT(8),
                  折扣率 FLOAT(8),
                  航班所属航班公司 VARCHAR(20),
                  PRIMARY KEY(航班，日期)
                  )
'''

HBH = ["K0001","Y7381","Z1919"]
QD = ["河北","湖南"]
ZD = ["山西","山东"]
RQ = ["140505050505","200505050505"]
QFSK = ["0911","1933"]
DDSK = ["1022","2235"]
SYZWS = [999,676]
PJ = [998,132]
ZKPJ = [333,67]
ZKL = [0.7,0.8]
HBSSGS = ["SH48A","JNSS"]

mylist = []
t = 0
for i in HBH:
    for j in QD:
        for k in ZD:
            for l in RQ:
                for m in QFSK:
                    for n in DDSK:
                        for o in SYZWS:
                            for p in PJ:
                                for q in ZKPJ:
                                    for r in ZKL:
                                        for s in HBSSGS:
                                            str = (i,j,k,l,m,n,o,p,q,r,s)
                                            mylist.append(str)
                                            t = t + 1

print(mylist)
doc = open('out.txt','w')
print(mylist,file=doc)
doc.close()