from django.contrib import admin
from freddit.models import Thread, Comment


class ThreadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('topic', )}

# Register your models here
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment)
