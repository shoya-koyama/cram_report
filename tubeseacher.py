import os
import googleapiclient.discovery

# YouTube Data APIの設定
api_service_name = "youtube"
api_version = "v3"
api_key = "秘密"


# YouTube Data APIのクライアントを作成
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

def search_videos_by_genre(genre, max_results=5):
    # ジャンルに基づいて動画検索のリクエストを作成
    request = youtube.search().list(
        part="snippet",
        q=genre,
        type="video",
        maxResults=max_results
    )

    # 動画検索のリクエストを実行し、レスポンスを取得
    response = request.execute()

    # 検索結果のタイトルとURLを表示
    for item in response["items"]:
        video_title = item["snippet"]["title"]
        video_url = "https://www.youtube.com/watch?v=" + item["id"]["videoId"]
        print(f"Title: {video_title}")
        print(f"URL: {video_url}")
        print()

# ジャンルに基づいて動画を検索して結果を表示
search_videos_by_genre("宇多田ヒカル", max_results=10)
