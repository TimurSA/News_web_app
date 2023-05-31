from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView  # ListView для вывода полностью всех записей из таблицы

# Create your views here.


def news_home(request):
    # news = Articles.objects.all()
    news = Articles.objects.order_by('-date') # Сортировка по записям в обратном порядке тк -
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm
    # fields = ['title', 'anons', 'full_text', 'date']


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    error=''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'


    form =  ArticlesForm()

    data ={
        'form': form,
        'error':error
    }
    return render(request, 'news/create.html', data)

