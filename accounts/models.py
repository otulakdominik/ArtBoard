from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birth_date = models.DateField(
        _('birth_date'),
        null=True,
    )

    avatar = models.ImageField(
        _('avatar'),
        blank=True,
        null=True,
    )

    facebook_url = models.URLField(
        _('facebook'),
        blank=True,
        null=True,
    )

    subscription = models.IntegerField(
        default=0,
    )

    email_confirmed = models.BooleanField(
        default=False,
    )


    class Meta:
        verbose_name = ('account')
        verbose_name_plural = ('accounts')


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
    instance.account.save()
