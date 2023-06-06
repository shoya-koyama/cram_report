let API_KEY_GOOGLE = 'AIzaSyAYSeZRkkIEUkvEc1Ut7UYs7q0lLRZds94';
let API_KEY_WEATHER = '****';

let map;
let marker;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 35.7804643, lng: 139.7151025 },
    zoom: 15
  });
  marker = new google.maps.Marker({
    map: map,
    draggable: true
  });
  marker.addListener('dragend', onMarkerDragEnd);
}

function findWeather() {
  let address = document.getElementById('input-address').value;
  let geocoder = new google.maps.Geocoder();
  geocoder.geocode({ address: address }, function (results, status) {
    if (status === 'OK') {
      let location = results[0].geometry.location;
      displayCoordinate(location);
    } else {
      alert('住所の取得に失敗しました。');
    }
  });
}

function displayCoordinate(location) {
  let latitude = location.lat();
  let longitude = location.lng();
  document.getElementById('latitude').textContent = latitude.toFixed(6);
  document.getElementById('longitude').textContent = longitude.toFixed(6);

  getWeather(latitude, longitude);
}

function getWeather(latitude, longitude) {
  let url =
    'https://api.openweathermap.org/data/2.5/weather?lat=' +
    latitude +
    '&lon=' +
    longitude +
    '&appid=' +
    API_KEY_WEATHER;

  fetch(url)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      displayWeather(data);
    })
    .catch(function (error) {
      alert('天気の取得に失敗しました。');
      console.log(error);
    });
}

function displayWeather(data) {
  let weather = data.weather[0].main;
  let temperature = data.main.temp;
  let humidity = data.main.humidity;
  let pressure = data.main.pressure;

  document.getElementById('td-weather').textContent = weather;
  document.getElementById('td-temperature').textContent = temperature;
  document.getElementById('td-humidity').textContent = humidity;
  document.getElementById('td-pressure').textContent = pressure;

  let cityName = data.name;
  document.getElementById('city').textContent = cityName;

  let latitude = data.coord.lat;
  let longitude = data.coord.lon;
  document.getElementById('latitude').textContent = latitude.toFixed(6);
  document.getElementById('longitude').textContent = longitude.toFixed(6);

  map.setCenter({ lat: latitude, lng: longitude });
  marker.setPosition({ lat: latitude, lng: longitude });
}

function onMarkerDragEnd() {
  let newPosition = marker.getPosition();
  displayCoordinate(newPosition);
}
