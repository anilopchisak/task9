from django.shortcuts import render, HttpResponse, get_object_or_404
from . import models
from django.views.generic import ListView, DetailView

class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context

class WorkerList(TitleMixin,ListView):
    model = models.Worker
    template_name = 'core/index.html'
    context_object_name = 'workers'
    title = 'Список работников'

    # def get_queryset(self):
    #     first_name = self.request.GET.get('name')
    #     qs =

class WorkerDetail(TitleMixin, DetailView):
    model = models.Worker
    template_name= 'core/worker_detail.html'
    context_object_name = 'worker'
    title = 'Работник'

def add_worker(request):
    title = 'Добавить работника'
    context = {'title': title}
    return render(request=request, template_name='core/add_worker.html',
                  context=context)

def best_worker(request):
    title = 'Сотрудник месяца'
    context = {'title': title}
    return render(request=request, template_name='core/best_worker.html',
                  context=context)

def check(request):
    user = request.user.username
    if user == 'polina':
        html = "<html> <body> <h1> Hi %s </h1> </body> </html>" %user
        return HttpResponse(html)
    return HttpResponse(status=403)