# Generated by Django 4.1.4 on 2023-05-30 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название отдела')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название должности')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=255, verbose_name='Второе имя')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('photo', models.ImageField(upload_to='workerphotos', verbose_name='Фото', blank=True)),
                ('kpi', models.IntegerField(verbose_name='KPI(%)')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.department', verbose_name='Отдел')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.position', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Workers',
            },
        ),
        migrations.CreateModel(
            name='TradeUnion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название профсоюза')),
                ('members', models.ManyToManyField(to='core.worker')),
            ],
            options={
                'verbose_name': 'Trade union',
                'verbose_name_plural': 'Trade unions',
            },
        ),
    ]
