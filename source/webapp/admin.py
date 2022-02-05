from django.contrib import admin

# Register your models here.
from webapp.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created']
    list_filter = ['created']
    search_fields = ['question', 'created']
    fields = ['question']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
