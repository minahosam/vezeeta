from django.contrib import admin
from .models import doctor_profile_1,category,place,doctor_reservation,subscribed_mails,rate_doctor
class doctorAdmin(admin.ModelAdmin):
    list_display=['user','name']
    prepopulated_fields={'slug':['name',]}
admin.site.register(doctor_profile_1)
admin.site.register(category)
admin.site.register(place)
admin.site.register(doctor_reservation)
admin.site.register(subscribed_mails)
admin.site.register(rate_doctor)