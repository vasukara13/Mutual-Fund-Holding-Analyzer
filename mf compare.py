import pandas as pd

#import requirments

class mf_compare:
    def __init__():
        pass
mf1=pd.read_csv('ppfc.csv')
mf2=pd.read_csv('icici bluechip.csv')


name_mf1=mf1["Invested In"].to_list() 
name_mf2=mf2["Invested In"].to_list()


common=[]
for i in name_mf1:
    print
    if i in name_mf2:
        common.append(i)
df=pd.DataFrame(common)
df.to_csv("ppfc and icici.csv")


