import pandas as pd
data= pd.read_csv("E:\main.csv")
from csv import reader
with open("E:\main.csv", 'r') as read_obj:
    csv_reader = reader(read_obj)
    x=0
    p=[]
    for row in csv_reader:
        if(x==0):
            p.append(row)
        if(x!=0):
            
            if(int(row[0])%10==0):
                if(x!=1):
                    l[1]=y
                    p.append(l)
                l=[0]*12
                l[0]=int(row[0])
                for i in range(1,len(row)):
                    if(i!=2):
                        l[i]+=int(row[i])
                y=row[1]
                
            else:
                for i in range(1,len(row)):
                    if(i!=2):
                        l[i]+=int(row[i])
                y=int(row[1])
        x+=1
    p.append(l)
    for i in p:
        i.remove(i[2])
import csv
with open('E:\outpu1.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerows(p)