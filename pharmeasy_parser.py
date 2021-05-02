from bs4 import BeautifulSoup
import requests
import string
import pandas as pd
final_list=[]
alphs=['%23']
for item in list(string.ascii_lowercase):
    alphs.append(item)
counts=[5,277,109,282,151,126,120,104,69,73,15,51,141,187,138,130,175,16,151,178,163,31,85,25,21,6,81]
for alpha,i in zip(alphs,counts):
    for t in range(i):
        url='https://pharmeasy.in/online-medicine-order/browse?alphabet={}&page={}'.format(alpha,t)
        r=requests.get(url)
        data=r.text
        soup=BeautifulSoup(data,'html.parser')
        title = soup.find("div", attrs={"class":'_3_nhL'})
        i=0;
        loca=[]

        for item in title:
            loca.append(item)
        concrete="https://pharmeasy.in"
        for link in loca:
            stri=str(link)
            start=stri.find("href=")+6
            end=stri.find(" rel")-1
            rough= concrete+stri[start:end]
            final_list.append(rough)
df=pd.DataFrame(final_list, columns=['Links'])
df.to_csv('Pharmeasy_links.csv')


