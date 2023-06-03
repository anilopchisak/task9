from django.db import models

class Department(models.Model):
    name = models.CharField(verbose_name='Название отдела', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

class Position(models.Model):
    name = models.CharField(verbose_name='Название должности', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

class Worker(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)
    surname = models.CharField(verbose_name='Второе имя', max_length=255, blank=True)
    depart = models.ForeignKey(Department, on_delete=models.DO_NOTHING, verbose_name='Отдел')
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING, verbose_name='Должность')
    phone = models.CharField(verbose_name='Номер телефона', null=True, blank=True, max_length=255)
    email = models.EmailField(verbose_name='E-mail')
    photo = models.ImageField(upload_to='workerphotos', verbose_name='Фото', blank=True)
    kpi = models.IntegerField(verbose_name='KPI(%)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

class TradeUnion(models.Model):
    name = models.CharField('Название профсоюза', max_length=255)
    members = models.ManyToManyField(Worker)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Trade union'
        verbose_name_plural = 'Trade unions'
