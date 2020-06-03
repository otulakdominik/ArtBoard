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
        verbose_name = _('account')
        verbose_name_plural = _('accounts')


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
    instance.account.save()


class Followers(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set')
    user_to = models.ForeignKey(User, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


User.add_to_class(
    'following', models.ManyToManyField('self', through=Followers, related_name='followers', symmetrical=False)
)


class Post(models.Model):
    title = models.CharField(
        _('title'),
        max_length=50,
    )

    slug = models.SlugField(
        _('slug'),
        max_length=120,
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    picture = models.ImageField(
        _('picture'),
    )

    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)

    created = models.DateTimeField(
        auto_now_add=True,
    )

    hashtag = models.ManyToManyField(Hashtag, blank=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    name = models.CharField(
        _('Hashtag'),
        max_length=30,
    )

    class Meta:
        verbose_name = _('hashtag')
        verbose_name_plural = _('hashtags')

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True, related_name='replies', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)
    description = models.TextField(
        _('description'),
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))
