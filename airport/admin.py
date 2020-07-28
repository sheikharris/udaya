from django.contrib import admin
from .models import airports_city,airport_img,airport_fact
# Register your models here.

class airports_city_show(admin.ModelAdmin):
    list_display=[
    'airport_name',
    'city'

    ]
    search_fields=['airport_name',]
    list_filter=["airport_name",'city'
               ]

class airport_img_show(admin.ModelAdmin):
    list_display=[
    'city',

    ]
    search_fields=['city']
    list_filter=["city"]

class airport_fact_show(admin.ModelAdmin):
    list_display=[
    'city',
    'title'

    ]
    search_fields=['title']
    list_filter=["title","city"]

admin.site.register(airports_city,airports_city_show)
admin.site.register(airport_img,airport_img_show)
admin.site.register(airport_fact,airport_fact_show)
