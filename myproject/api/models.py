from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.SmallIntegerField(null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    speciality = models.CharField(max_length=255, null=True, blank=True)
    residence = models.CharField(max_length=255, null=True, blank=True)
    height = models.SmallIntegerField(null=True, blank=True)
    weight = models.SmallIntegerField(null=True, blank=True)
    lead_hand = models.CharField(max_length=255, null=True, blank=True)
    diseases = models.CharField(max_length=255, null=True, blank=True)
    smoking = models.BooleanField(null=True, blank=True)
    alcohol = models.CharField(max_length=255, null=True, blank=True)
    sport = models.CharField(max_length=255, null=True, blank=True)
    insomnia = models.BooleanField(null=True, blank=True)
    current_health = models.SmallIntegerField(null=True, blank=True)
    gaming = models.BooleanField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="api_user_groups",  # Уникальное имя для обратной связи
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="api_user_permissions",  # Уникальное имя для обратной связи
        related_query_name="user",
    )
    
class TestNSI(models.Model):
    test_id = models.BigIntegerField(primary_key=True)
    test_name = models.CharField(max_length=255)
    title_all = models.CharField(max_length=255, null=True)
    title_correct = models.CharField(max_length=255, null=True)

class TestResult(models.Model):
    test = models.ForeignKey(TestNSI, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    try_number = models.SmallIntegerField()
    number_all_answers = models.IntegerField(null=True, blank=True)
    number_correct_answers = models.IntegerField(null=True, blank=True)
    complete_time = models.DurationField(null=True, blank=True)
    accuracy = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
