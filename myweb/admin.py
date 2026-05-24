from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  date_hierarchy = "updated_date"
  empty_value_display = "---"
  list_display = ("name", "email", "subject", "updated_date")
  list_filter = ("email",)
  search_fields = ("name", "email", "subject")