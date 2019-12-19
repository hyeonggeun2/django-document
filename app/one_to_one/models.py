from django.db import models


class Place(models.Model):
    address = models.CharField('주소', max_length=200)

    def __str__(self):
        return f'Place (address: {self.address})'


class Restaurant(models.Model):
    place = models.OneToOneField(Place, verbose_name='장소', on_delete=models.CASCADE)
    name = models.CharField('식당명', max_length=30)
    rating = models.IntegerField('평점', default=0)

    def __str__(self):
        return f'{self.name} (평점: {self.rating})'

# class Shop(models.Model):
#     TYPE_CHOICES = (
#         ('convenience', '편의점'),
#         ('game', '게임샵'),
#     )
#     place = models.OneToOneField(Place, verbose_name='장소', on_delete=models.CASCADE)
#     name = models.CharField('상점명', max_length=30)
#     type = models.CharField('상점유형', choices=TYPE_CHOICES, max_length=20)
#
#     def __str__(self):
#         return f'{self.name} (유형: {self.get_type_display()})'