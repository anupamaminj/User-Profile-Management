from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('mobile_number', 'first_name', 'last_name', 'email', 'city', 'state', 'occupation', 'last_updated')
    search_fields = ('mobile_number', 'email', 'first_name', 'last_name')
    list_filter = ('state', 'gender', 'occupation')
