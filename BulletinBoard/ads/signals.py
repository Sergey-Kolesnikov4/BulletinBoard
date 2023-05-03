from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Responses,Ads
from BulletinBoard import settings
from django.contrib.auth.models import User



@receiver(post_save, sender=Responses)
def notify_responses(sender, instance,created,**kwargs):
    if instance.status==False:
        html_content = render_to_string('responses_created_email.html',
            {
                'text': 'Новый отклик к твоей статье',
                'ads': f'{instance.ads.title}'
            }
        )
        to=[instance.ads.author.email]
    else:
        html_content = render_to_string('responses_changed_email.html',
                                        {
                                            'text': 'Автор принял твой отклик к статье',
                                            'ads': f'{instance.ads.title}'
                                        }
                                        )
        to = [instance.responses_user.email]


    msg = EmailMultiAlternatives(
    subject = f'Уведомление',
    body = '',
    from_email = settings.DEFAULT_FROM_EMAIL,
    to = to
    )
    msg.attach_alternative(html_content, 'text/html')

    msg.send()


@receiver(post_save, sender=Ads)
def notify_ads(sender, instance,created,**kwargs):
    authors=User.objects.all().values_list('email', flat=True)
    mail =set(authors)

    html_content=render_to_string(
        'new_ads.html',
        {
            'link':settings.SITE_URL,
            'ads': instance,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Новое объявление',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=mail
    )

    msg.attach_alternative(html_content,'text/html')
    msg.send()