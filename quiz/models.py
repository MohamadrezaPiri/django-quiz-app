from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']

    def __str__(self):
        return self.name


class Quizzes(models.Model):

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
        ordering = ['id']

    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    title = models.CharField(
        max_length=255, default='New Quiz', verbose_name='Quiz Title')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name='Last Update')

    class Meta:
        abstract = True


class Question(Updated):

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['id']

    DIFFICULTY_FUNDAMENTAL = 0
    DIFFICULTY_BEGINNER = 1
    DIFFICULTY_INTERMEDIATE = 2
    DIFFICULTY_ADVANCED = 3
    DIFFICULTY_EXPERT = 4

    DIFFICULTY_CHOICES = [
        (DIFFICULTY_FUNDAMENTAL, 'Fundamental'),
        (DIFFICULTY_BEGINNER, 'Beginner'),
        (DIFFICULTY_INTERMEDIATE, 'Intermediate'),
        (DIFFICULTY_ADVANCED, 'Advanced'),
        (DIFFICULTY_EXPERT, 'Expert'),
    ]

    TYPE_MULTIPLE = 0

    TYPE_CHOICES = [
        (TYPE_MULTIPLE, 'Multiple Choice')
    ]

    quiz = models.ForeignKey(
        Quizzes, null=True, related_name='question', on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, verbose_name='Title')
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES,
                                     default=DIFFICULTY_FUNDAMENTAL, verbose_name='Difficulty')
    technique = models.IntegerField(
        choices=TYPE_CHOICES, default=TYPE_MULTIPLE, verbose_name='Type Of Question')
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name='Date Created')
    is_active = models.BooleanField(
        default=False, verbose_name='Active Status')

    def __str__(self):
        return self.title


class Answer(Updated):

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ['id']

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, verbose_name='Answer Text')
    is_right = models.BooleanField(default=False)
