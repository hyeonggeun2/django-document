from django.db import models


class UserMixin(models.Model):
    class Meta:
        abstract = True


class BaseUser(models.Model):
    is_superuser = models.BooleanField(default=False)

    def show_pk(self):
        print(self.pk)


class NormalUser(BaseUser):
    class Meta:
        proxy = True


class SuperUserManage(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_superuser=True)


class SuperUser(BaseUser):
    # 기본값 objects = models.Manager()
    objects = SuperUserManage()

    class Meta:
        proxy = True

    def delete_user(self, pk):
        BaseUser.objects.get(pk=pk).delete()
