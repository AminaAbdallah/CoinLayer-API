# CoinlayerAPI 
A package using coinlayerAPI
## Three main functions:
1. Fetch_data_InSpecific_TimeFrame(acess_key,start_date,end_date,symbol ): 
    * acess_key: the key that we get from coinLayerAPI.
    * start_date : the start date of the period that we're looking for, example: 2018-02-01.
    * end_date   : the end date of the period that we're looking for, example: 2019-02-01.
    * symbol: the cryptocurrency such us BTC.
    
    
2.Fetch_historical_data(acess_key,date):
    * acess_key: the key that we get from coinLayerAPI.
    * date: the date of the historical data that we're looking for.
   
3.Currency_conversion(access_key,crytpcurrency1,cyptcurrecy2,amount):
     * acess_key: the key that we get from coinLayerAPI.
     * crytpcurrency1: the currency that we want to convert.
     * crytpcurrency1: the currency that we want to convert to.
     * amount: The amount of currency to convert.
     
# How to use the package:
  1. import  CoinlayerAPI 
