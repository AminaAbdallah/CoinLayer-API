import json
import pandas
import requests




def Currency_conversion(acess_key,crytpcurrency1,cyptcurrecy2,amount):
    Currency_conversion_url = 'http://api.coinlayer.com/convert ? access_key = acess_key & from = crytpcurrency1 & to = cyptcurrecy2 & amount = amount '
    
    Currency_conversion_payload={'access_key':acess_key , 'from' : crytpcurrency1 , 'to' : cyptcurrecy2 , 'amount' : amount}
    response = requests.get(url=HCurrency_conversion_url,params=Currency_conversion_payload)
    
    pretty_json_output = json.dumps(response.json(), indent=4)
    response_json_string = json.dumps(response.json())
    response_dict = json.loads(response_json_string)
    return response_dict

