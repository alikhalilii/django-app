from django.contrib import admin
from .models import Post , Category , Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
  date_hierarchy = "created_date"
  empty_value_display = "---"
  list_display = ("title", "author", "counted_views", "status", "login_required", "published_date", "created_date")
  list_filter = ("status", "author")
  search_fields = ["title", "content"]
  summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
  date_hierarchy = "created_date"
  empty_value_display = "---"
  list_display = ("post", "name", "email", "subject", "is_approved",  "created_date", "updated_date")
  list_filter = ("post", "is_approved")
  search_fields = ["post", "name"]

admin.site.register(Category)
admin.site.register(Post , PostAdmin)
admin.site.register(Comment , CommentAdmin)