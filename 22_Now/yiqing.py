import requests
import json
import time
import pandas as pd
import matplotlib.pyplot as plt

stamp=time.time()
#print(int((stamp)*1000))


url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=&_=%d'%int((stamp)*1000)
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
r = requests.get(url)
if r.status_code==200:
    d = r.json()
    results=json.loads(d['data'])
else:
    print('not got')
print(type(results))
print(results.keys())
#print(results['chinaDayList'])
#pd 做成excel表格形式的数据展示
df_china_daily=pd.DataFrame(results['chinaDayList'],columns=['date','confirm','suspect','dead','heal','deadRate','healRate'])
#print(df_china_daily)
x=df_china_daily['date'].values#时间
confirm=df_china_daily['confirm'].values#确诊患者
suspect=df_china_daily['suspect'].values#疑似患者
dead=df_china_daily['dead'].values#死亡
heal=df_china_daily['heal'].values#治愈

plt.figure(figsize=(12,8))
plt.plot(x,confirm,marker='*',label='confirm')
plt.plot(x,suspect,marker='^',label='suspect')
plt.plot(x,dead,marker='^',label='dead')
plt.plot(x,heal,marker='^',label='heal')
plt.legend()
plt.show()


