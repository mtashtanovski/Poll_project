from django.db import models


# Create your models here.
class Poll(models.Model):
    question = models.CharField(
        max_length=500,
        verbose_name='Опрос'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return f"{self.id}. {self.question}"

    class Meta:
        db_table = 'Polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    option = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Текст варианта'
    )
    poll = models.ForeignKey(
        'webapp.Poll',
        on_delete=models.CASCADE,
        related_name='choices',
        verbose_name='Опрос'
    )

    def __str__(self):
        return f"{self.id}. {self.option}"

    class Meta:
        db_table = 'Choices'
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'


class Answer(models.Model):
    poll = models.ForeignKey(
        'webapp.Poll',
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name="Опрос"
    )
    option = models.ForeignKey(
        'webapp.Choice',
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name="Вариант ответа"
    )

    class Meta:
        db_table = 'Answers'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
