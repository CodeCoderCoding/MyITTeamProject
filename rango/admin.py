from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Used to automatically fill in the alias when entering the category name
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# register Category on admin page
admin.site.register(Category, CategoryAdmin)
# register Page on admin page
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)