from django.db import models
from datetime import date

from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    DISABILITY_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Prefer not to say', 'Prefer not to say'),
    ]

    ACTIVITY_CHOICES = [
        ('Low', 'Low'),
        ('Light', 'Light'),
        ('Moderate', 'Moderate'),
        ('High', 'High'),
    ]

    DIET_CHOICES = [
        ('Vegetarian', 'Vegetarian'),
        ('Non-vegetarian', 'Non-vegetarian'),
        ('Vegan', 'Vegan'),
        ('Jain', 'Jain'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()

    height = models.FloatField()
    weight = models.FloatField()

    activity_level = models.CharField(
        max_length=20, choices=ACTIVITY_CHOICES, blank=True
    )

    disability = models.CharField(
        max_length=30,
        choices=DISABILITY_CHOICES,
        default='Prefer not to say'
    )

    accessibility_needs = models.TextField(blank=True)
    health_conditions = models.TextField(blank=True)
    food_allergies = models.TextField(blank=True)

    dietary_preference = models.CharField(
        max_length=30, choices=DIET_CHOICES, blank=True
    )

    health_goal = models.CharField(max_length=100)

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) <
            (self.date_of_birth.month, self.date_of_birth.day)
        )

        return self.full_name

# Create your models here.
class DailyTracker(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    date = models.DateField(default=timezone.localdate)

    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    fruits = models.BooleanField(default=False)
    activity = models.BooleanField(default=False)
    relaxation = models.BooleanField(default=False)
    sleep = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user.username} - {self.date}"

