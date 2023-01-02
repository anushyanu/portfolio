from requests import get
from pprint import PrettyPrinter

BASE_URL="https://api.apilayer.com/"
API_KEY="1MZQrHhfyLaH827DN8LbsMfEHWsUBkGh"

#curl --request GET 'https://api.apilayer.com/exchangerates_data/live?base=USD&symbols=EUR,GBP' \
#--header 'apikey: YOUR API KEY'

payload = {}
headers= {
  "apikey": "1MZQrHhfyLaH827DN8LbsMfEHWsUBkGh"
}

printer = PrettyPrinter()

def get_currencies(from_currency, to_currency, value):
	endpoint= f"exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={value}&apikey" #base=USD&symbols=EUR,GBP"
	url = BASE_URL + endpoint
	data = get(url,headers=headers,data=payload).json()['result']

	printer.pprint(data)


get_currencies('GBP','USD',100)
get_currencies('GBP','EUR',100)
get_currencies('GBP','INR',100)