from django.contrib.auth.models import User
from django.db import models

class HairProfile(models.Model):
    HAIR_TYPES = [
        ('straight', 'Straight'),
        ('wavy', 'Wavy'),
        ('curly', 'Curly'),
        ('coily', 'Coily'),
    ]

    HAIR_LENGTHS = [
        ('short', 'Short'),
        ('medium', 'Medium'),
        ('long', 'Long'),
    ]

    POROSITY_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    BRITTLENESS_LEVELS = [
        ('none', 'None'),
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    hair_type = models.CharField(max_length=50, choices=HAIR_TYPES)
    hair_length = models.CharField(max_length=50, choices=HAIR_LENGTHS)
    porosity = models.CharField(max_length=50, choices=POROSITY_LEVELS)
    brittleness = models.CharField(max_length=50, choices=BRITTLENESS_LEVELS)
    dyed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nickname}'s Hair Profile"

class JournalEntry(models.Model):
    ENTRY_TYPES = [
        ('wash', 'Миття волосся'),
        ('mask', 'Маска'),
        ('other', 'Інше'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entries')
    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPES)
    notes = models.TextField(blank=True)
    photo = models.ImageField(upload_to='journal_photos/', blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.entry_type} ({self.date})"
