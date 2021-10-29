from django.urls import path
from .views import NewsViews, NewsDetails

urlpatterns = [
      path('', NewsViews.as_view()),
      path('<int:pk>', NewsDetails.as_view()),

]