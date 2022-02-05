from django.db import models


# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=100, null=False, blank=False, verbose_name='Опрос')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.pk}: {self.question}"

    class Meta:
        db_table = 'questions'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    answer = models.CharField(max_length=30, null=False, blank=False, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='choices', verbose_name='Опрос')

    def __str__(self):
        return f"{self.answer}"

    class Meta:
        db_table = 'choices'
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'
