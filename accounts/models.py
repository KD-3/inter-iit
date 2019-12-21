from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class ContractorProfile(models.Model):
    name = models.CharField(max_length=50, help_text="Name of the the contractor")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contractor_id = models.CharField(max_length=32, help_text="Enter the contractor id")
    rating = models.DecimalField(max_digits=2, decimal_places=2)
    projects_taken = models.IntegerField()
    projects_completed = models.IntegerField()
    phone = models.CharField(max_length=15, help_text="For phone numbers outside India, please add country code")
    email = models.EmailField()

    def __str__(self):
        return self.name


class PublicProfile(models.Model):
    name = models.CharField(max_length=50, help_text="Enter your name")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, help_text="Enter your city")
    email = models.EmailField()
    phone = models.CharField(max_length=15, help_text="For phone numbers outside India, please add country code")


class RoadProfile(models.Model):
    name = models.CharField(max_length=32)
    contractor = models.ForeignKey(ContractorProfile, on_delete=models.CASCADE)
    condition_bad = models.BooleanField(default=False)
    # rating = models.DecimalField(decimal_places=2)


class Feedback(models.Model):
    author = models.ForeignKey(PublicProfile, on_delete=models.CASCADE)
    road = models.ForeignKey(RoadProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
