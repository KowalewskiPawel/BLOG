from django.urls import path
from .views import HomeView, ArticleDetailView, CategoryView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('category/<str:cats>/', CategoryView, name='categories'),
]

urlpatterns += staticfiles_urlpatterns()
