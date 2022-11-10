from django.contrib import admin
from .models import Volunteer, Partner, ContactPage, Help_choices, MailList, Post, ImageCategory, ImageFile

class VolunteerPageAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'country')

class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

class PartnerPageAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone_number', 'company', 'country', 'area_of_interest', 'any_other_details')

admin.site.register(Volunteer, VolunteerPageAdmin)
admin.site.register(Partner, PartnerPageAdmin)
admin.site.register(ContactPage, ContactPageAdmin)
admin.site.register(Help_choices)
admin.site.register(MailList)
admin.site.register(Post)
admin.site.register(ImageCategory)
admin.site.register(ImageFile)