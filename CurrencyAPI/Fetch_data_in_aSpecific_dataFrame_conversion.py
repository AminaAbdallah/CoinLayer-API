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
