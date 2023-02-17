# Generated by Django 3.2 on 2023-02-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=32, verbose_name='Вид животного')),
                ('name', models.CharField(max_length=32, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('image', models.ImageField(upload_to='uploads/% Y/% m/% d/', verbose_name='Изображение')),
            ],
        ),
    ]
