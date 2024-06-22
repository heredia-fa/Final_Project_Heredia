from .models import News
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class News_list(ListView):
    model = News
    template_name = 'landing_news/landing.html'
    context_object_name = 'news'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset= News.objects.all()
        if query:
            queryset = News.objects.filter(title__icontains=query)
        return queryset.order_by('-original_date')    
    




class News_detail(LoginRequiredMixin,DetailView):
    model = News
    context_object_name = 'new'


class News_create(LoginRequiredMixin,CreateView):
    model = News
    template_name = 'landing_news/news_create.html'
    fields = ["title" , "description", "picture"]
    success_url =  reverse_lazy("landing_news:landing")


class News_update(LoginRequiredMixin,UpdateView):
    model = News
    template_name = 'landing_news/news_update.html'
    fields = ('__all__')
    success_url =  reverse_lazy("landing_news:landing")
    context_object_name = 'new'

class News_delete(LoginRequiredMixin,DeleteView):
    model = News
    template_name = 'landing_news/news_delete.html'
    context_object_name = 'new'
    success_url =  reverse_lazy("landing_news:landing")


def about(req):
    return render(req, "landing_news/about.html")