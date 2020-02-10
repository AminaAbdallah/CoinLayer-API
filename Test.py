



from CurrencyAPI.Fetch_historical_data import Fetch_historical_data
from CurrencyAPI.currency_conversion import Currency_conversion
from CurrencyAPI.Fetch_data_in_aSpecific_timeFrame_conversion import Fetch_data_InSpecific_TimeFrame
import os


access_key = os.environ.get('b36407a99f24a168e534d190404b18f7')



Fetch_historical_data('access_key','2018-02-01')


Currency_conversion('access_key','BTC','USD',10)

Fetch_data_InSpecific_TimeFrame('access_key','2018-04-01','2018-04-30','BTC')




