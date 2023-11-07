from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404, JsonResponse
from django.utils import timezone
from cram.models import Article, Comment
from django.http import JsonResponse

from googleapiclient.discovery import build
#import os
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings


# YouTube Data APIの設定
api_service_name = "youtube"
api_version = "v3"
api_key = settings.YOUTUBE_API_KEY
youtube = build(api_service_name, api_version, developerKey=api_key)

# Create your views here.
def index(request):
    videos = []
    if request.method == 'POST':
        if 'keyword' in request.POST:
            keyword = request.POST['keyword']
            videos = search_videos(keyword, max_results=10)

        elif 'title' in request.POST and 'text' in request.POST:
            article = Article(title=request.POST['title'], body=request.POST['text'])
            article.save()
            return redirect(detail, article.id)

    articles = Article.objects.order_by('-posted_at')
    context = {
        "articles": articles,
        "videos": videos,  
    }

    return render(request, 'project/index.html', context)






def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')

    if request.method == 'POST':
        comment = Comment(article=article, text=request.POST['text'])
        comment.save()

    context = {
        'article': article,
        'comments': article.comments.order_by('-posted_at')
    }
    return render(request, 'project/detail.html', context)


def update(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')
    if request.method == 'POST':
        article.title = request.POST['title']
        article.body = request.POST['text']
        article.save()
        return redirect(detail, article.id)
    context = {
        'article': article
    }

    return render(request, 'project/edit.html', context)


def delete(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')
    
    article.delete()
    
    return redirect(index)

# @login_required
# def delete(request, article_id):
#     try:
#         article = Article.objects.get(pk=article_id)

#         # 記事のオーナーか、スーパーユーザーのみが削除できるようにします
#         if request.user != article.owner and not request.user.is_superuser:
#             messages.error(request, 'あなたにはこの記事を削除する権限がありません。')
#             return redirect('index')

#         article.delete()
#         messages.success(request, '記事が正常に削除されました。')

#     except Article.DoesNotExist:
#         messages.error(request, '該当する記事が見つかりませんでした。')

#     return redirect('index')


def like(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        article.like += 1
        article.save()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    
    return redirect(detail, article_id)



def api_like(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        article.like += 1
        article.save()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    result = {
        'id' : article_id,
        'like' : article.like
    }

    return JsonResponse(result)

def search_videos(keyword, max_results=5):
    request = youtube.search().list(
        part="snippet",
        q=keyword,
        type="video",
        maxResults=max_results,
        relevanceLanguage="ja", 
        order="viewCount"  
    )
    response = request.execute()
    videos = []
    for item in response["items"]:
        video_title = item["snippet"]["title"]
        video_url = "https://www.youtube.com/watch?v=" + item["id"]["videoId"]
        thumbnail_url = item["snippet"]["thumbnails"]["default"]["url"]
        video_description = item["snippet"]["description"]
        videos.append({
            "title": video_title, 
            "url": video_url, 
            "thumbnail": thumbnail_url, 
            "description": video_description
        })
    return videos

def upload_video(request):
    image_url = None

    if request.method == 'POST' and 'file' in request.FILES:
        myfile = request.FILES['file']
        fs = FileSystemStorage(location=settings.UPLOAD_FOLDER)
        filename = fs.save(myfile.name, myfile)
        image_url = fs.url(filename)

    return render(request, 'index.html', {'image_url': image_url})
    # メッセージ付きのページにリダイレクトするか、メッセージとともにここでテンプレートをレンダリングすることもできます。


def room(request, room_name):
    return render(request, "project/room.html", {"room_name": room_name})

def speech_view(request):
    return render(request, 'project/speech_template.html')

def word_read(request):
    return render(request, 'project/word_read.html')