from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class City(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    intro = models.TextField(default="introduction")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Scenery(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 300

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)
    intro = models.TextField("introduction")
    picture = models.ImageField(upload_to='scenery_images', blank=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class UserLikedCity(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    intro = models.TextField(default="City introduction.")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(UserLikedCity, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class UserLikedScenery(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 300

    city = models.ForeignKey(UserLikedCity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)
    intro = models.TextField("Scenery introduction")
    picture = models.ImageField(upload_to='user_scenery_images', blank=True)

    def __str__(self):
        return self.title
