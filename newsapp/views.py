from django.views.generic import ListView, DetailView
from .models import NewsModel
from datetime import datetime



class NewsViews(ListView):
    model = NewsModel
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    queryset = NewsModel.objects.order_by('-dateCreation')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context[
            'value1'] = None
        return context

class Post(DetailView):
    model = NewsModel
    template_name = 'flatpages\post.html'
    context_object_name = 'post'

