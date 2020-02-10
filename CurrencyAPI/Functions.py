import json
import pandas
import requests




def Fetch_data_InSpecific_TimeFrame(acess_key,start_date,end_date,symbol ):
    HistoricalData_url = 'http://api.coinlayer.com/timeframe? access_key = acess_key & start_date = start_date& end_date = end_date& symbols = symbol '
    
    HistoricalData_payload={'access_key':acess_key,'start_date':start_date, 'end_date' : end_date, 'symbols':  symbol}
    response = requests.get(url=HistoricalData_url,params=HistoricalData_payload)
    
    pretty_json_output = json.dumps(response.json(), indent=4)
    response_json_string = json.dumps(response.json())
    response_dict = json.loads(response_json_string)
    return response_dict
  
  
def Fetch_historical_data(acess_key,date):
    HistoricalData_url = 'http://api.coinlayer.com/date ? access_key = acess_key'
    HistoricalData_payload={'access_key' : acess_key,'YYYY-MM-DD':date}
    response = requests.get(url=HistoricalData_url,params=HistoricalData_payload)
    
    pretty_json_output = json.dumps(response.json(), indent=4)
    response_json_string = json.dumps(response.json())
    response_dict = json.loads(response_json_string)
    return response_dict
  
def Currency_conversion(access_key,crytpcurrency1,cyptcurrecy2,amount):
    Currency_conversion_url = 'http://api.coinlayer.com/convert ? access_key = acess_key & from = crytpcurrency1 & to = cyptcurrecy2 & amount = amount '
    
    Currency_conversion_payload={'access_key':acess_key , 'from' : crytpcurrency1 , 'to' : cyptcurrecy2 , 'amount' : amount}
    response = requests.get(url=HCurrency_conversion_url,params=Currency_conversion_payload)
    
    pretty_json_output = json.dumps(response.json(), indent=4)
    response_json_string = json.dumps(response.json())
    response_dict = json.loads(response_json_string)
    return response_dict
