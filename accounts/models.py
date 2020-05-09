from django.db import models
from django.utils.translation import gettext_lazy as _


class Acount(models.Model):

    name = models.CharField(
        _('name'),
        max_length=70,
    )

    last_name = models.CharField(
        _('last_name'),
        max_length=70,
    )

    username = models.CharField(
        _('username'),
        max_length=35,
    )

    birth_date = models.DateField(
        _('birth_date'),
    )

    email = models.EmailField(
        _('username'),
        max_length=100,
    )

    avatar = models.ImageField(
        _('avatar'),
        required=False,
    )

    facebook_url = models.URLField(
        _('facebook'),
        required=False,
    )
