from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy

from core import models, forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

    def get_queryset(self):
        name = self.request.GET.get('name')
        kpi = self.request.GET.get('kpi')
        qs = models.Worker.objects.all()
        if name or kpi:
            return qs.filter(Q(name__icontains=name) | Q(kpi__contains=kpi))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.WorkerSearch(self.request.GET or None)
        return context

class WorkerDetail(TitleMixin, DetailView):
    model = models.Worker
    template_name= 'core/worker_detail.html'
    context_object_name = 'worker'
    title = 'Работник'

class WorkerCreate(TitleMixin, CreateView):
    model = models.Worker
    template_name = 'core/worker_create.html'
    title = 'Добавить работника'
    context_object_name = 'worker'
    fields = '__all__'
    success_url = reverse_lazy('core:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.WorkerActions
        return context

class WorkerUpdate(TitleMixin, UpdateView):
    model = models.Worker
    template_name = 'core/worker_update.html'
    title = 'Изменить информацию о работнике'
    context_object_name = 'worker'
    fields = '__all__'
    success_url = reverse_lazy('core:index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.WorkerActions
        return context

class WorkerDelete(TitleMixin, DeleteView):
    model = models.Worker
    template_name = 'core/worker_delete.html'
    title = 'Удалить работника'
    context_object_name = 'worker'
    fields = '__all__'
    success_url = reverse_lazy('core:index')

def best_worker(request):
    title = 'Сотрудник месяца'
    context = {'title': title}
    return render(request=request, template_name='core/best_worker.html',
                  context=context)
