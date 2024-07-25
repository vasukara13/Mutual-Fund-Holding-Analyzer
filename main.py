#impoert file here and call staritng function here

from price_info import *




if __name__ =="main":
    
    holding_csv=pd.read_csv("ppfc.csv")
    mf_name="Parag Parikh Flexi Cap"

    stock_info(holding_csv,mf_name)