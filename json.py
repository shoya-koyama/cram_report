import json
import requests

def data_to_geojson(data_chunk):
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    
    for item in data_chunk:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [item["longitude"], item["latitude"]]
            },
            "properties": {
                "name": item["name"]
            }
        }
        geojson["features"].append(feature)
    
    return geojson

def fetch_and_split_data(api_url):
    # APIからJSONデータを取得
    response = requests.get(api_url)
    response.raise_for_status()
    json_data = response.json()
    
    # 'data'キーの下のリストを取得
    data_list = json_data['data']

    # データを50個ずつに分割
    chunks = [data_list[i:i + 50] for i in range(0, len(data_list), 50)]

    # 分割したデータをGeoJSON形式で別々のファイルに保存
    for index, chunk in enumerate(chunks):
        geojson_chunk = data_to_geojson(chunk)
        with open(f'splitted_{index + 1}.geojson', 'w') as file:
            json.dump(geojson_chunk, file)

# 実行
api_url = 'https://your-api-url.com/data'
fetch_and_split_data(api_url)

###############################
import json

def process_data(json_data):
    data_dict = {}
    
    for entry in json_data['data']:
        A_ID = entry.pop('A_ID', None)
        if A_ID:
            if A_ID not in data_dict:
                data_dict[A_ID] = {'A_ID': A_ID}
            data_dict[A_ID].update(entry)

    return list(data_dict.values())

def split_and_save(json_data, prefix='output'):
    processed_data = process_data(json_data)
    chunks = [processed_data[i:i + 50] for i in range(0, len(processed_data), 50)]

    for index, chunk in enumerate(chunks):
        with open(f'{prefix}_{index + 1}.json', 'w') as file:
            json.dump({"data": chunk}, file)

# 実行
with open('your_large_json_file.json', 'r') as f:
    json_data = json.load(f)

split_and_save(json_data)
