from django.urls import path
from .views import NewsAPIView, NewsDetail
urlpatterns = [
    path('news/', NewsAPIView.as_view(), name="news list api"),
    path('news/<int:pk>/', NewsDetail.as_view(), name="news detail api")
]