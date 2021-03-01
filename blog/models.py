from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Category(models.Model):
    status = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=status, default='Draft')

    def __str__(self):
        return self.name



class Blog(models.Model):
    status = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    )

    tag = (
        ('Technology', 'Technology'),
        ('Software', 'Software'),
        ('Cyber Security', 'Cyber Security'),
        ('Programming', 'Programming'),
        ('Python', 'Python'),
        ('Javascript', 'Javascript'),
        ('Java', 'Java'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog', blank=True)
    tag = MultiSelectField(choices=tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=status, default=status[0][0])
    view = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=500)
    website = models.URLField(max_length=1000, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name