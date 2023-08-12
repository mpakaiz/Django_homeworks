from django.contrib import admin

# Register your models here.
from phones.models import Phone

admin.site.register(Phone)


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'release_date', 'lte_exists', 'slug']
    list_display_links = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
