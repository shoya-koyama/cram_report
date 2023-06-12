import os
import googleapiclient.discovery
from flask import Flask, render_template

# YouTube Data APIの設定
api_service_name = "youtube"
api_version = "v3"
api_key = "秘密"

# YouTube Data APIのクライアントを作成
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

app = Flask(__name__)

def search_videos(keyword, max_results=5):
    # 動画検索のリクエストを作成
    request = youtube.search().list(
        part="snippet",
        q=keyword,
        type="video",
        maxResults=max_results,
        relevanceLanguage="ja",  # 日本語の動画を検索
        order="viewCount"  # 人気順にソート
    )

    # 動画検索のリクエストを実行し、レスポンスを取得
    response = request.execute()

    # 検索結果のタイトルとURLをリストとして格納
    videos = []
    for item in response["items"]:
        video_title = item["snippet"]["title"]
        video_url = "https://www.youtube.com/watch?v=" + item["id"]["videoId"]
        videos.append({"title": video_title, "url": video_url})

    return videos

@app.route("/")
def index():
    keyword = "宇多田ヒカル"
    max_results = 10
    videos = search_videos(keyword, max_results)
    return render_template("tube.html", videos=videos)

if __name__ == "__main__":
    app.run()
