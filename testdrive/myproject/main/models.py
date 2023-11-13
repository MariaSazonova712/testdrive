from django.db import models


class Drive(models.Model):
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=50)
    email = models.CharField('Почта', max_length=50)
    auto = models.CharField('Машина', max_length=50)
    task = models.TextField('Комментарий')

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
