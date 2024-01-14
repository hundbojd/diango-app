from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(null=True, blank=True, max_length=150)
    city = models.CharField(null=True, blank=True, max_length=20)
    social = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            if img.height < img.width:
                # make square by cutting off equal amounts left and right
                left = (img.width - img.height) / 2
                right = (img.width + img.height) / 2
                top = 0
                bottom = img.height
                img = img.crop((left, top, right, bottom))
                img.thumbnail((300, 300))
                img.save(self.image.path)

            elif img.width < img.height:
                # make square by cutting off bottom
                left = 0
                right = img.width
                top = 0
                bottom = img.width
                img = img.crop((left, top, right, bottom))
                img.thumbnail((300, 300))
                img.save(self.image.path)
            else:
                # already square
                img.thumbnail((300, 300))
                img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)
