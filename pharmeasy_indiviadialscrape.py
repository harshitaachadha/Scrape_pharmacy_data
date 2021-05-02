from bs4 import BeautifulSoup
import requests
import re
import csv
import pandas as pd
final_list=[]
i=0
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def appendrow(list_of_elem):
    # Open file in append mode
    with open('pharmeasy_first_10k.csv','a+') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


appendrow(['Qunatity_and_Packform', 'Manufacturer', 'Medname', 'Discount Price', 'Sales Price', 'Discount percentage',
           'Composition', 'Image'])

with open("Pharmeasy_links.csv",'r') as file:
    csvreader=csv.reader(file)
    count=0
    for row1 in csvreader:
        if count>=20000:
            break
        count+=1
        temp_list = []
        row=list(row1)
        url=row[1]
        r=requests.get(url)
        data=r.text
        soup=BeautifulSoup(data,'html.parser')


        #To find Quantity and Packform
        qnp=str(soup.find("div", attrs={'class':'_36aef'}))
        Quantity_and_packform=cleanhtml(qnp)
        temp_list.append(Quantity_and_packform)

        #To find the manufacturer
        manu=str(soup.find("div", attrs={"class":'_3JVGI'}))
        Manufacturer=cleanhtml(manu)[3:]
        temp_list.append(Manufacturer)

        # To find the name of the medicine
        name= str(soup.find("h1",attrs={"class":'ooufh'}))
        Medname=cleanhtml(name)
        temp_list.append(Medname)

        #To find the discount price
        inter_dp= str(soup.find("div",attrs={"class":'_1_yM9'}))
        Discount_Price=cleanhtml(inter_dp)
        temp_list.append(Discount_Price)

        # To find sales price
        inter_sp= str(soup.find("span",attrs={"class":'_31Agc'}))
        Actual_Price=cleanhtml(inter_sp)
        temp_list.append(Actual_Price)

        # to find discount percentage
        inter_dis= str(soup.find("div",attrs={"class":'_306Fp'}))
        Discount=cleanhtml(inter_dis)
        temp_list.append(Discount)

        # To find the composition
        comp=str(soup.find("div", attrs={"class":'_3Phld'}))
        Composition=cleanhtml(comp)
        comp_list=Composition.split(' + ')
        temp_list.append(comp_list)

        # To find the image
        try:
            img=soup.find("img",attrs={"class":"_150ST"})
            Image=img.get('src')
            temp_list.append(Image)

        except:
            temp_list.append("None")

        #final_list.append(temp_list)
        appendrow(temp_list)
        #flag+=1

#df=pd.DataFrame(final_list,columns=['Qunatity_and_Packform','Manufacturer','Medname','Discount Price','Sales Price','Discount percentage','Composition','Image'])
#df.to_csv('Pharmeasy_data_23_March_2021(0-20k).csv')

