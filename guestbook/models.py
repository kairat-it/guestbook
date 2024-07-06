from django.db import models

class GuestbookEntry(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('blocked', 'Заблокировано'),
    ]

    name_author = models.CharField(max_length=100, verbose_name="Имя автора")
    email_author = models.EmailField(verbose_name="Почта автора")
    entry_text = models.TextField(verbose_name="Текст записи")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Время редактирования")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name="Статус"
    )

    def __str__(self):
        return f"{self.name_author} - {self.status}"
