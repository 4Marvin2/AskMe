from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Профиль')
    avatar = models.ImageField(upload_to='avatars/%y/%m/%d', verbose_name='Аватар')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.user_id.get_username()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Tag(models.Model):
    tag = models.CharField(unique=True, max_length=16, verbose_name='Тег')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Question(models.Model):
    profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст вопроса')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE, verbose_name='Профиль')
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.TextField(verbose_name='Текст ответа')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_correct = models.BooleanField(default=False, verbose_name='Флаг правильного ответа')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class LikeQuestion(models.Model):
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='Вопрос')
    profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE, verbose_name='Профиль')
    is_like = models.BooleanField(default=True, verbose_name='Лайк или дизлайк')

    def __str__(self):
        action = 'дизлайкнул'
        if self.is_like:
            action = 'лайкнул'
        return f'{self.profile_id.user_id.get_username()} {action} вопрос: {self.question_id.title}'

    class Meta:
        verbose_name = 'Лайк вопроса'
        verbose_name_plural = 'Лайки вопросов'


class LikeAnswers(models.Model):
    answer_id = models.ForeignKey('Answer', on_delete=models.CASCADE, verbose_name='Ответ')
    profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE, verbose_name='Профиль')
    is_like = models.BooleanField(default=True, verbose_name='Лайк или дизлайк')

    def __str__(self):
        action = 'дизлайкнул'
        if self.is_like:
            action = 'лайкнул'
        return f'{self.profile_id.user_id.get_username()} {action} ответ: {self.answer_id.text}'

    class Meta:
        verbose_name = 'Лайк ответа'
        verbose_name_plural = 'Лайки ответов'
