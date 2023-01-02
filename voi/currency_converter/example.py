import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=GBP&amount=50.00"
#url = "https://api.apilayer.com/exchangerates_data/convert?"

payload = {}
headers= {
  "apikey": "1MZQrHhfyLaH827DN8LbsMfEHWsUBkGh"
}

response = requests.request("GET", url, headers=headers, data = payload)
#print(requests.request("GET"),url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

print(result)
