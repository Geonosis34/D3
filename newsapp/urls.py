from django.urls import path
from .views import NewsViews, Post

urlpatterns = [
      path('', NewsViews.as_view()),
      path('<int:pk>', Post.as_view()),
]