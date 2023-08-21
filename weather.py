import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        
        return {
            "Temperature": temp,
            "Pressure": pressure,
            "Humidity": humidity,
            "Description": weather_description
        }
    else:
        return {"Error": data["message"]}

# 以下のように関数を使用できます
# api_key = "YOUR_API_KEY"
# city_name = "Tokyo"
# print(get_weather(city_name, api_key))

"""もちろん、このコードをステップごとに説明いたします。

モジュールのインポート:
python
Copy code
import requests
requestsモジュールは、ウェブ上のAPIやウェブページなどからデータを取得する際に非常に便利なPythonのライブラリです。
天気を取得する関数の定義:
python
Copy code
def get_weather(city_name, api_key):
get_weather という関数を定義しています。この関数は2つの引数を取ります: city_name(都市名)とapi_key(Open Weather MapのAPIキー)。
APIのベースURLの設定:
python
Copy code
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
Open Weather Mapの天気情報を取得するための基本的なURLを設定しています。
完全なURLの作成:
python
Copy code
    complete_url = f"{base_url}q={city_name}&appid={api_key}"
base_url、都市名(city_name)、APIキー(api_key)を使用してAPIリクエストのための完全なURLを作成しています。
APIリクエストの実行:
python
Copy code
    response = requests.get(complete_url)
    data = response.json()
requests.get関数を使用してAPIのURLにリクエストを送信しています。
.json()メソッドを使用して、応答をJSON形式のデータとして解析しています。
データの解析:
python
Copy code
    if data["cod"] == 200:
        ...
    else:
        return {"Error": data["message"]}
APIからの応答には、codというキーが含まれており、これはHTTPステータスコードを示しています。200は成功を意味します。
応答が成功した場合（codが200の場合）、天気に関連する情報を取得しています。それ以外の場合は、エラーメッセージを返しています。
天気情報の取得:
python
Copy code
        main = data["main"]
        weather = data["weather"][0]
        ...
        return {
            "Temperature": temp,
            "Pressure": pressure,
            "Humidity": humidity,
            "Description": weather_description
        }
応答データから気温、気圧、湿度、天気の説明などの情報を取得しています。
最後に、これらの情報を含む辞書を返しています。
関数の使用例:
python
Copy code
# api_key = "YOUR_API_KEY"
# city_name = "Tokyo"
# print(get_weather(city_name, api_key))
この部分はコメントアウトされていますが、APIキーと都市名を設定して、上記の関数を使用して天気情報を取得する方法を示しています。
全体として、このコードはOpen Weather Map APIを利用して、指定した都市の天気情報を取得するものです。"""

import requests
import pandas as pd

def get_weather_df(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        
        # データをデータフレームに変換
        weather_data = {
            "City": [city_name],
            "Temperature": [temp],
            "Pressure": [pressure],
            "Humidity": [humidity],
            "Description": [weather_description]
        }
        df = pd.DataFrame(weather_data)
        return df
    else:
        print(data["message"])
        return pd.DataFrame()

# 使用例
# api_key = "YOUR_API_KEY"
# city_name = "Tokyo"
# weather_df = get_weather_df(city_name, api_key)
# print(weather_df)
