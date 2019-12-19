from django.db import models


class WPSUser(models.Model):
    # models.CASCADE 1:N 에서 1이 삭제됐을 때 N을 모두 삭제한다.
    #       .PROTECT N이 있으면 삭제가 안된다. // .SET_NULL N을 NULL 채워서 존재시킨다.
    #       .SET_DEFAULT N을 정해서 채운다. // .SET 커스텀 옵션
    instructor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='student_set')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
