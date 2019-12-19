from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    # DB 에서는 column / Django 에서는 field 라고 부른다.
    # choices 를 사용하면 DB 에서는 작은 공간을 사용하지만, user 가 선택할 때는 길게 나온다.
    shirt_size = models.CharField('셔츠 사이즈', max_length=1, choices=SHIRT_SIZES, help_text='셔츠 사이즈 이다')
    first_name = models.CharField('이름', max_length=30)
    last_name = models.CharField('성', max_length=30)