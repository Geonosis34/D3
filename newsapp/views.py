from django.views.generic import ListView, DetailView
from .models import NewsModel
from datetime import datetime



class NewsViews(ListView):
    model = NewsModel
    template_name = 'flatpages/news.html'
    context_object_name = 'news'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context[
            'value1'] = None
        return context


class NewsDetails(DetailView):
    model = NewsModel
    template_name = 'flatpages/news.html'
    context_object_name = 'news'