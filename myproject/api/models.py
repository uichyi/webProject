from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=128) 
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

    def __str__(self):
        return self.username

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password_hash)
    
class TestNSI(models.Model):
    test_id = models.BigIntegerField(primary_key=True)
    test_name = models.CharField(max_length=255)
    title_all = models.CharField(max_length=255, null=True)
    title_correct = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.test_name

class TestResult(models.Model):
    test = models.ForeignKey(TestNSI, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    try_number = models.SmallIntegerField(null=True, blank=True)
    number_all_answers = models.IntegerField(null=True, blank=True)
    number_correct_answers = models.IntegerField(null=True, blank=True)
    complete_time = models.DurationField(null=True, blank=True)
    accuracy = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.test.test_name}"
