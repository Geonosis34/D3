from django.views.generic import ListView, DetailView
from .models import Product
from datetime import datetime


class ProductList(ListView):
    model = Product
    template_name = 'flatpages/products.html'
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context[
            'value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'flatpages/products.html'
    context_object_name = 'product'

