from django.db import models


class Gallery(models.Model):
    # gallery_id = models.
    name = models.CharField('Название галереи', max_length=200, null=True)
    city = models.CharField('Город', max_length=70, null=True)
    country = models.CharField('Страна', max_length=50, null=True)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Painter(models.Model):
    name = models.CharField('Художник', max_length=200, null=True)
    country = models.CharField('Страна', max_length=70, null=True)

    class Meta:
        verbose_name = 'Хужожник'
        verbose_name_plural = 'Художники'


class Picture(models.Model):
    name = models.CharField('Название картины', max_length=200, null=True)
    genre = models.CharField('Жанр', max_length=70, null=True)
    year = models.DateField('Год написания', null=True)
    painter = models.ForeignKey(Painter, on_delete=models.CASCADE, null=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картины'