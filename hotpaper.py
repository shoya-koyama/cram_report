import requests

def search_hotpepper_restaurants(api_key, keyword):
    base_url = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    params = {
        "key": api_key,
        "keyword": keyword,
        "format": "json"
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data["results"]["results_returned"] > 0:
        return data["results"]["shop"]
    else:
        print("No results found.")
        return []

# 使用例
# api_key = "YOUR_API_KEY"
# keyword = "ラーメン"
# restaurants = search_hotpepper_restaurants(api_key, keyword)
# for restaurant in restaurants:
#     print(restaurant["name"], "-", restaurant["address"])
