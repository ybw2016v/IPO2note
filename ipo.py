import requests as r
import re
import json
import time

def getipoinfo():
    """
    获取当日新股
    """
    dog_re=re.compile(',data:(.*)},\r')
    dog_re2=re.compile('data:[(.*)]')

    dog_cont=r.get("http://data.eastmoney.com/xg/xg/default.html")
    dog_html=dog_cont.content
    # f=open('sd.html','wb')
    # f.write(dog_html)
    # f.close()
    # print(dog_html)

    dog_html2=str(dog_html,'gbk')
    # print(dog_html2)
    dog_e=dog_re.findall(dog_html2)
    # print(dog_e)
    dog_f=json.loads(dog_e[0])
    # for sdk in dog_f:
    #     print(sdk)
    #     pass
    # print(dog_f[0:10])
    dog_info=[]

    for dog_list in dog_f:
        dog_date=dog_list['purchasedate']
        dog_dates=time.strptime(dog_date,"%Y-%m-%dT%H:%M:%S")
        dog_localtime = time.localtime(time.time())
        # print(dog_dates.tm_mday)
        if dog_localtime.tm_yday==dog_dates.tm_yday:
            dog_l={}
            dog_l['name']=dog_list['securityshortname']
            dog_l['DM']=dog_list['subcode']
            dog_l['sc']=dog_list['sc']
            if dog_l['sc']=='cyb':
                dog_l['sc']='创业板'
                pass
            if dog_l['sc']=='kcb':
                dog_l['sc']='科创板'
                pass
            if dog_l['sc']=='sh':
                dog_l['sc']='上海'
                pass
            if dog_l['sc']=='sz':
                dog_l['sc']='深圳'
                pass
            # dog_l['']=dog_list['']
            dog_info.append(dog_l)
            pass
    # print(dog_info)
    if dog_info==[]:
        dog_s='今日无新股'
    else:
        dog_s=''
        for dog_d in dog_info:
            dog_s=dog_s+'{} {} {}\n'.format(dog_d['DM'],dog_d['name'],dog_d['sc'])
            pass
        pass
    return dog_s




