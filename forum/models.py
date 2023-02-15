from datetime import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField('Заголовок записи', max_length=35, blank=False)
    description = models.TextField("Текст Записи", max_length=500, blank=False)
    date = models.DateTimeField("Дата и время публикации", default=datetime.now)
    img = models.ImageField("Картинка (необязательно)", blank=True, default='missing_img.jpg')

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.title}'


class Comments(models.Model):
    text_comments = models.TextField('Текст комментария', max_length=200)
    date = models.DateTimeField("Дата и время публикации", default=datetime.now)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.text_comments}'


class ChangeLogPost(models.Model):
    title_changelog = models.CharField('Заголовок changelog', max_length=200, blank=False)
    desc_changelog = models.CharField('Описание changelog', max_length=200, blank=False)
    date_changelog = models.DateTimeField('Дата changelog', blank=False)

    def __str__(self):
        return f'{self.title_changelog}'
