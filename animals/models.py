from django.db import models


class Animal(models.Model):
    kind = models.CharField(max_length=32, verbose_name="Вид животного")
    name = models.CharField(max_length=32, verbose_name="Имя")
    description = models.TextField(verbose_name="Описание")
    birthday = models.DateField(verbose_name="День рождения")
    image = models.ImageField(upload_to ='uploads/%Y/%m/%d/', verbose_name="Изображение")

    def __str__(self):
        return f'{self.kind} {self.name}'

