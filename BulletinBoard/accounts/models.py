from django.db import models
from django.contrib.auth.models import User


class OneTimeCode(models.Model):
    code=models.CharField(max_length=4,unique=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    class Meta:
        app_label='accounts'

    def __str__(self):
        return f'{self.code}'
