import requests

def get_dmm_items(api_id, affiliate_id, keyword):
    base_url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "DMM.com",
        "service": "mono",
        "floor": "dvd",
        "hits": 10,  # 取得件数
        "keyword": keyword,
        "output": "json"
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data["result"]["status"] == 200:
        return data["result"]["items"]
    else:
        print("Error:", data["result"]["message"])
        return []

# 使用例
# api_id = "YOUR_API_ID"
# affiliate_id = "YOUR_AFFILIATE_ID"
# keyword = "キーワード"
# items = get_dmm_items(api_id, affiliate_id, keyword)
# for item in items:
#     print(item["title"], "-", item["URL"])
