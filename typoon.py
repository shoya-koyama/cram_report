import folium

def plot_typhoon_on_map(typhoon_data):
    # 地図の初期化（日本の中心を基点とする）
    m = folium.Map(location=[37.5, 137.5], zoom_start=5)

    for data in typhoon_data:
        # 台風の位置をマーカーとしてプロット
        marker = folium.Marker(
            location=[data['latitude'], data['longitude']],
            popup=f"Typhoon Name: {data['name']}\nWind Speed: {data['wind_speed']} km/h",
            icon=folium.Icon(icon="cloud")
        )
        marker.add_to(m)

        # 暴風域を円として表現
        folium.Circle(
            location=[data['latitude'], data['longitude']],
            radius=data['storm_radius'] * 1000,  # この例では半径をメートル単位としています
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(m)

    # 地図を保存
    m.save('typhoon_map.html')

# サンプルデータ
typhoon_data_sample = [
    {"name": "Typhoon A", "latitude": 35.0, "longitude": 135.0, "wind_speed": 100, "storm_radius": 50},
    {"name": "Typhoon B", "latitude": 30.0, "longitude": 140.0, "wind_speed": 80, "storm_radius": 40}
]

plot_typhoon_on_map(typhoon_data_sample)
