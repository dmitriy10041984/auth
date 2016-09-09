from django.db import models

"""
from django.contrib.auth.models import User
from tinymce import models as tinymce_model


# Create your models here.
class Contact(models.Model):

    subject = models.CharField(max_length=100, verbose_name="Тема")
    sender = models.EmailField(max_length=254, verbose_name="Отправитель")
    message = tinymce_model.HTMLField(verbose_name="Сообщение")
    #флаг, который пользователь устанавливает, если хочет получить копию сообщения себе на e-mail
    #(булевая переменная, представляющая собой необязательный к заполнению чекбокс).
    copy = models.BooleanField(required=False, verbose_name="Получить копию письма")

    class Meta():
        db_table = 'contact'
        ordering = ['subject']
        verbose_name = "Контактная форма"
        verbose_name_plural = "Данные контактных форм"

    def __str__(self):
        return self.subject

"""








