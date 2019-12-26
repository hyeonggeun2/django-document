from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Restaurant(Place):
    # place1_ptr = models.OneToOneField(Place1, parent_link=True)
    # 이렇게 상속을 해서 만든다면 위를 기본적으로 가지게 됨
    hot_dogs = models.BooleanField(default=False)
    pizza = models.BooleanField(default=False)
    # related_name='restaurant',
    # related_name='restaurant_set'

    place_ptr = models.OneToOneField(Place, parent_link=True, related_query_name='restaurant_by_oto', on_delete=models.CASCADE)

    # query_name 을 이용해서 접근하면 Place 의 속성값들에 대해 탐색할 수 있는데, 그 이름이 같아버리니까 바꿔주어야 함
    near_place = models.ManyToManyField(Place, related_query_name='restaurant_by_near_places')

    def __str__(self):
        return f'{self.name} (핫도그: {self.hot_dogs}, 피자: {self.pizza})'
