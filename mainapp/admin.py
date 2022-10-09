from django.contrib import admin
from .models import Volunteer, Partner, ContactPage, Help_choices, MailList, Post, ImageCategory, ImageFile

admin.site.register(Volunteer)
admin.site.register(Partner)
admin.site.register(ContactPage)
admin.site.register(Help_choices)
admin.site.register(MailList)
admin.site.register(Post)
admin.site.register(ImageCategory)
admin.site.register(ImageFile)