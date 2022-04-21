from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name = 'home'),
    path('diary/create/', DiaryCreateView.as_view(), name = 'diary-create'),
    path('diary/<int:pk>/', DiaryRetrieveView.as_view(), name = 'diary-retrieve'),
    path('diary/update/<int:pk>/', DiaryUpdateView.as_view(), name = 'diary-update'),
    path('diary/delete/<int:pk>/', DiaryDeleteView.as_view(), name = 'diary-delete'),
    path('chapter/create/', ChapterCreateView.as_view(), name = 'chapter-create'),
    path('chapter/<int:pk>/', ChapterRetrieveView.as_view(), name = 'chapter-retrieve'),
    path('chapter/update/<int:pk>/', ChapterUpdateView.as_view(), name = 'chapter-update'),
    path('chapter/delete/<int:pk>/', ChapterDeleteView.as_view(), name = 'chapter-delete'),
]