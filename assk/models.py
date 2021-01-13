from django.db import models


from django.contrib.auth.models import User



class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.TimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.user.get_username()

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

class Post(models.Model):
    author = models.ForeignKey('Account', on_delete = models.CASCADE, verbose_name= 'Автор')
    time_posted = models.TimeField(auto_now_add=True, blank=True)
    text = models.TextField(verbose_name = 'текст вопроса')
    title = models.TextField(verbose_name = 'заголовок вопроса')
    tags = models.ManyToManyField('Tags', verbose_name = 'Тэги', null = True, blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    author = models.ForeignKey('Account', on_delete = models.CASCADE, verbose_name= 'Автор')
    title = models.TextField(verbose_name = 'заголовок ответа')
    text = models.TextField(verbose_name = 'текст ответа')
    time_posted = models.TimeField(auto_now_add=True, blank=True)
    question = models.ForeignKey('Post', on_delete = models.CASCADE, verbose_name= 'Вопрос')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Tags(models.Model):
    name = models.CharField(verbose_name= 'Имя тэга',max_length=64)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'