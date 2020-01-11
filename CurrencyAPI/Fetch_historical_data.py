import json
import pandas
import requests




def Fetch_historical_data(acess_key,date):
    HistoricalData_url = 'http://api.coinlayer.com/date ? access_key = acess_key'
    HistoricalData_payload={'access_key' : acess_key,'YYYY-MM-DD':date}
    response = requests.get(url=HistoricalData_url,params=HistoricalData_payload)
    
    pretty_json_output = json.dumps(response.json(), indent=4)
    response_json_string = json.dumps(response.json())
    response_dict = json.loads(response_json_string)
    return response_dict






    '''
    
    i=0
    
    while i< len(response_dict ):
        rates=response_dict['rates']
        print(rates,'\n')
        i=i+1
    return rates'''



