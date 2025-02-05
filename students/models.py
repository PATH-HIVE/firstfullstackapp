from django.db import models

# Create your models here.


class Institution(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    PROGRAMMING_LANGUAGES = [
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('JavaScript', 'JavaScript'),
        ('Python', 'Python'),
        ('Ruby', 'Ruby'),
        ('React', 'React'),
        ('SQL', 'SQL'),
    ]
    
    institution = models.CharField(max_length=255) 
    programming_language = models.CharField(max_length=20, choices=PROGRAMMING_LANGUAGES)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

