from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )

    # SECTION ACCESS
    can_view_puller = models.BooleanField(default=False)
    can_view_button = models.BooleanField(default=False)

    # FIELD-LEVEL ACCESS (puller list/detail এর মধ্যে)
    can_view_price = models.BooleanField(default=False)
    can_view_body_parts = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Profile"


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()




class BodyParts(models.Model):

    body_code = models.CharField(
        max_length=50,
        unique=True
    )

    body_name = models.CharField(
        max_length=200
    )

    body_size = models.CharField(
        max_length=100,
        blank=True
    )

    body_weight = models.DecimalField(
        max_digits=10,
        decimal_places=8,
        blank=True,
        null=True
    )

    body_price = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.body_code} - {self.body_name}"

    @property
    def formatted_weight(self):
        if self.body_weight is None:
            return None

        return format(
            self.body_weight,
            'f'
        ).rstrip('0').rstrip('.')

class PullerCategory(models.Model):

    CATEGORY_CHOICES = [
        ('special', 'Special Puller'),
        ('regular', 'Regular Puller'),
        ('da', 'DA Puller'),
        ('dalh', 'DALH Puller'),
    ]

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        unique=True
    )

    category_name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.category_name


class Puller(models.Model):

    puller_code = models.CharField(
        max_length=50,
        unique=True
    )

    puller_name = models.CharField(
        max_length=200
    )

    puller_details = models.TextField(
        blank=True
    )


    category = models.ForeignKey(
        PullerCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pullers'
    )


    puller_size = models.CharField(
        max_length=100,
        blank=True
    )

    puller_length = models.CharField(
        max_length=100,
        blank=True
    )

    puller_width = models.CharField(
        max_length=100,
        blank=True
    )

    puller_thickness = models.CharField(
        max_length=100,
        blank=True
    )

    puller_inner_dia = models.CharField(
        max_length=100,
        blank=True
    )

    puller_outer_dia = models.CharField(
        max_length=100,
        blank=True
    )

    puller_weight = models.DecimalField(
    max_digits=10,
    decimal_places=8,
    blank=True,
    null=True
    )

    puller_price = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        blank=True,
        null=True
    )

    body_parts = models.ManyToManyField(
        BodyParts,
        blank=True,
        related_name='pullers'
)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.puller_code} - {self.puller_name}"

    @property
    def formatted_weight(self):
        if self.puller_weight is None:
            return None
        return format(self.puller_weight, 'f').rstrip('0').rstrip('.')



class PullerImage(models.Model):

    puller = models.ForeignKey(
        Puller,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='pullers/'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.puller.puller_code} - Image"







