#!python3
import requests as r
import re
import json

dog_re=re.compile('data:(.*),font:{')
dog_re2=re.compile('data:[(.*)]')

dog_cont=r.get("http://data.eastmoney.com/kzz/default.html")
dog_html=dog_cont.text
# f=open('sd.html','wb')
# f.write(dog_html)
# f.close()
print(dog_html)
dog_res=dog_re.findall(dog_html)
print(dog_res[0])
# dogres2=dog_re2.findall(dog_res[0])
# print(dogres2)