from django import forms, core
from core import models

class WorkerSearch(forms.Form):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Поиск по имени работника', 'class': 'form-group'})
    )
    kpi = forms.IntegerField(
        required=False,
        min_value=0,
        max_value=300,
        widget=forms.NumberInput(
            attrs={'placeholder': 'Поиск по kpi', 'class': 'form-group'})
    )
    # depart = forms.ModelChoiceField(
    #     required=False,
    #     label='Поиск по отделу',
    #     queryset=models.Worker.objects.order_by().values_list('depart', flat=True).distinct(),
    #     widget=forms.Select(
    #         attrs={'id':'DepartmentDropDownList', 'class': 'form-group'})
    # )

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.isnumeric() or ('/' in name):
            raise core.exceptions.ValidationError('Имя должно состоять из букв')
        return name

    class Meta:
        model = models.Worker
        fields = '__all__'

class WorkerActions(forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.isdigit():
            raise core.exceptions.ValidationError('Имя должно состоять из букв')
        return name

    class Meta:
        model = models.Worker
        fields = ['name', 'surname', 'depart', 'position', 'phone', 'email', 'photo', 'kpi']