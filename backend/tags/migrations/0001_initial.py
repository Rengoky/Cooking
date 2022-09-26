# Generated by Django 4.1.1 on 2022-09-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название тэга')),
                ('slug', models.SlugField(help_text='Ссылка тега', unique=True, verbose_name='Ссылка')),
                ('color', models.CharField(default='#ffffff', max_length=7, unique=True, verbose_name='Цвет тэга')),
            ],
            options={
                'verbose_name': 'Тэг',
                'db_table': 'tag',
            },
        ),
    ]