import requests
import pybitflyer

# 価格取得
res = requests.get('https://api.bitflyer.jp/v1/ticker?product_code=ETH_JPY')
jsonData = res.json()
print('ETH_JPY  = ' + "¥{:,.0f}".format(jsonData["ltp"]))
price = jsonData["ltp"]

#0.01の日本円
price_thousand = price * 0.01
print('0.01 ETH = ¥', round(price_thousand))


# API認証
api = pybitflyer.API(api_key="*****",
                     api_secret="*****")

# 買い注文
api.sendchildorder(
    product_code="ETH_JPY",
    child_order_type="MARKET",
    side="BUY",
    #最低単位が0.01
    size= 0.01,
    minute_to_expire=100000,
    time_in_force="GTC"
)

print('end')

