from django.contrib import admin
from .models import Volunteer, Mentor, ContactPage, Help_choices, MailList, Post, ImageCategory, ImageFile

admin.site.register(Volunteer)
admin.site.register(Mentor)
admin.site.register(ContactPage)
admin.site.register(Help_choices)
admin.site.register(MailList)
admin.site.register(Post)
admin.site.register(ImageCategory)
admin.site.register(ImageFile)