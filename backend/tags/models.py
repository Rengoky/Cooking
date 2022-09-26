from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название тэга',
                            unique=True, null=False)

    slug = models.SlugField(verbose_name='Ссылка', unique=True, help_text='Ссылка тега')

    color = models.CharField(max_length=7, default='#ffffff',
                             unique=True, verbose_name='Цвет тэга')


    class Meta:
        db_table = 'tag'
        verbose_name = 'Тэг'