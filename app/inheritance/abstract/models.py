from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    abc = models.CharField(max_length=10)

    # 실제로 존재하지 않고 상속만 해줄 것이다.
    class Meta:
        abstract = True
        ordering = ['name']


class Student(CommonInfo):
    school = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} (학교: {self.school})'


class Instructor(CommonInfo):
    academy = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} (학원: {self.academy})'
