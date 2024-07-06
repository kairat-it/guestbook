# Generated by Django 5.0.6 on 2024-07-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestbookEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_author', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('email_author', models.EmailField(max_length=254, verbose_name='Почта автора')),
                ('entry_text', models.TextField(verbose_name='Текст записи')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Время редактирования')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=10, verbose_name='Статус')),
            ],
        ),
    ]
