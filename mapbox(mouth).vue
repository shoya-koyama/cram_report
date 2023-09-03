<template>
  <div>
    <div ref="map" style="width: 100%; height: 400px;"></div>
  </div>
</template>

<script>
import mapboxgl from 'mapbox-gl';
import axios from 'axios';

export default {
  name: 'MapboxComponent',
  data() {
    return {
      map: null,
      geojsonUrl: 'YOUR_GEOJSON_URL_HERE',
    };
  },
  mounted() {
    this.loadMap();
  },
  methods: {
    async loadMap() {
      // GeoJSON データの取得
      const response = await axios.get(this.geojsonUrl);
      const geojsonData = response.data;

      // Mapbox の初期化
      mapboxgl.accessToken = 'YOUR_MAPBOX_ACCESS_TOKEN_HERE';
      this.map = new mapboxgl.Map({
        container: this.$refs.map,
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [139.6917, 35.6895],  // 東京の緯度経度
        zoom: 10
      });

      this.map.on('load', () => {
        // 台風の進路上の点を追加
        this.map.addSource('points', {
          'type': 'geojson',
          'data': geojsonData
        });

        this.map.addLayer({
          'id': 'points',
          'type': 'circle',
          'source': 'points',
          'paint': {
            'circle-radius': 6,
            'circle-color': '#B42222'
          }
        });

        // マウスオーバーイベントを追加
        this.map.on('mouseenter', 'points', (e) => {
          if (e.features.length > 0) {
            const feature = e.features[0];
            const radius = feature.properties.radius;  // 暴風域の半径情報

            // 暴風域を表す円を描画
            const circleSource = {
              'type': 'geojson',
              'data': {
                'type': 'FeatureCollection',
                'features': [feature]
              }
            };

            // すでに同じIDのソースやレイヤーが存在する場合、それを削除
            if (this.map.getLayer('hover-circle')) {
              this.map.removeLayer('hover-circle');
              this.map.removeSource('hover-circle');
            }

            this.map.addSource('hover-circle', circleSource);

            this.map.addLayer({
              'id': 'hover-circle',
              'type': 'circle',
              'source': 'hover-circle',
              'paint': {
                'circle-radius': radius,
                'circle-opacity': 0.5,
                'circle-color': '#33A1C9'
              }
            });
          }
        });

        // マウスが点から移動したとき、円を削除
        this.map.on('mouseleave', 'points', () => {
          if (this.map.getLayer('hover-circle')) {
            this.map.removeLayer('hover-circle');
            this.map.removeSource('hover-circle');
          }
        });
      });
    }
  }
};
</script>

<style>
/* 必要に応じてスタイルを追加 */
</style>
