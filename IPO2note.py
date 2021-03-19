#!python3
import requests as r
import re
import json
import time
from ipo import getipoinfo

key=""
URL="https://m.dogcraft.cn/api/notes/create"



dog_re=re.compile('data:(.*),font:{')
dog_re2=re.compile('data:[(.*)]')

dog_cont=r.get("http://data.eastmoney.com/kzz/default.html")
dog_html=dog_cont.text
# f=open('sd.html','wb')
# f.write(dog_html)
# f.close()
# print(dog_html)
dog_res=dog_re.findall(dog_html)
# print(dog_res[0])
# dogres2=dog_re2.findall(dog_res[0])
# print(dogres2)
dog_json=json.loads(dog_res[0])
# print(dog_json[0])
dog_info=[]

for dog_list in dog_json:
    dog_date=dog_list['STARTDATE']
    dog_dates=time.strptime(dog_date,"%Y-%m-%dT%H:%M:%S")
    dog_localtime = time.localtime(time.time())
    if dog_localtime.tm_yday==dog_dates.tm_yday:
        dog_l={}
        dog_l['cname']=dog_list['CORRESNAME']
        dog_l['DM']=dog_list['SWAPSCODE']
        # dog_l['']=dog_list['']
        # dog_l['']=dog_list['']
        dog_info.append(dog_l)
        pass
    
    # print(dog_dates)
    # dog_l={}
    # dog_l['name']=dog_list['SNAME']
    # dog_l[]

    pass
# print(dog_info)
if dog_info==[]:
    dog_s='今日无可转债'
else:
    dog_s=''
    for dog_d in dog_info:
        dog_s=dog_s+'{} {}\n'.format(dog_d['DM'],dog_d['cname'])
        pass
    pass

dog_today=time.strftime("%Y-%m-%d", time.localtime())


# print(dog_str)
dog_ls=getipoinfo()
# print(dog_ls)
# 
# 

dog_str='今日打新 {}\n可转债:\n{}\n新股：\n{}'.format(dog_today,dog_s,dog_ls)

# print(dog_str)

if time.localtime().tm_wday <= 4:
    print('可能是交易日')
    payload={'text':dog_str,"localOnly":False,"visibility":"public","viaMobile":False,"i":key}
# payload={'text':dog_str,"localOnly":True,"visibility":"public","viaMobile":False,"i":key}
    sd=r.post(URL,json=payload)
    print(sd.text)
else:
    print('一定不是交易日')
# key=


