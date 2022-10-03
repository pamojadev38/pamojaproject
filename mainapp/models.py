from django.db import models
from .countries import COUNTRIES
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from PIL import Image

class Help_choices(models.Model):
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Help Choices'

    def __str__(self):
        return self.description

class Volunteer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    country = models.CharField(max_length=50, choices=COUNTRIES)
    what_can_you_help_with = models.ManyToManyField(Help_choices)
    any_other_area_you_would_like_to_help = models.CharField(max_length=300)
    why_would_you_like_to_help = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.email}"

class Mentor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, blank=True,null=True)
    company = models.CharField(max_length=50)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    area_of_interest = models.CharField(max_length=50)
    any_other_details = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.email}"


class ContactPage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Page'

    def __str__(self):
        return f"{self.name} - {self.email}"

class MailList(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Mail List'

    def __str__(self):
        return self.email


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class ImageCategory(models.Model):
    category_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Image Categories'

    def __str__(self):
        return self.category_name

class ImageFile(models.Model):
    image_name = models.ImageField(upload_to='gallery_pics/', blank=True, default='default-banner.jpg')
    category = models.ForeignKey(ImageCategory, on_delete=models.PROTECT)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Image Files'
    
    def __str__(self):
        return str(self.image_name)
