from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/delete', views.delete, name='delete'),
    path('<int:article_id>/update', views.update, name='update'),
    path('<int:article_id>/like', views.like, name='like'),
    path('api/articles/<int:article_id>/like', views.api_like),
    path('chat/<str:room_name>/',views.room, name='room'),
    path('speech_view/',views.speech_view, name='speech_view'),
    path('word_read/',views.word_read, name='word_read'),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    path('fetch-google-calendar-event-title/', views.fetch_google_calendar_event_title, name='fetch_google_calendar_event_title'),

]

