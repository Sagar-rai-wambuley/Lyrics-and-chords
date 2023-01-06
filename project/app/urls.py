from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.Home, name='home'),
    path('content/<int:id>/', views.Lyric_And_Chord, name='content'),
    path('request/', views.Song_Request, name='request'),
    path('search/', views.Search, name='search'),
    path('aboutus/', views.Aboutus, name='aboutus'),
    path('section/', views.chord_Section, name='section'),
] + static(settings.MEDIA_URL, document=settings.MEDIA_ROOT)
