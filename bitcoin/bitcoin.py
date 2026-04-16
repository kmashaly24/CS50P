import sys
if len(sys.argv) == 1:
    print("Missing command_line argument")
    sys.exit
else:
    try:
        n = float(sys.argv[1])
    except:
        print("command_line argument is not a number")
        sys.exit

import requests
import json

try:
    respone = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    result = respone.json()
    print(json.dumps(result, indent = 2))

    price = result['bpi']['USD']['rate_float']*n

    print(f"${price:,}")
except requests.RequestException:
    pass
