from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Ads(models.Model):

    blacksmith = 'bs'
    potions_master = 'pm'
    spell_master = 'sm'

    ADTYPE = [
            (blacksmith, 'Кузнецы'),
            (potions_master, 'Мастера зельеварения'),
            (spell_master, 'Мастера заклинаний')
        ]

    title = models.CharField(max_length=34)
    content = RichTextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=2, choices=ADTYPE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        app_label = 'ads'

    def __str__(self):
        return f'{self.title} :{self.content}'

    def get_absolute_url(self):
        return f'/ads/{self.id}'



class Responses(models.Model):
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    responses_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        app_label = 'ads'

    def __str__(self):
        return f'{self.comment}'

