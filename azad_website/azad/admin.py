from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
admin.site.register(Event)
admin.site.register(Coveritem)
admin.site.register(Imagemodel)
admin.site.register(Notice)
admin.site.register(Achievements)
admin.site.register(Team)
admin.site.register(Year)
admin.site.register(Contact)
admin.site.register(Para)
admin.site.register(azad_boarders)
admin.site.register(complaints)
admin.site.register(book)
admin.site.register(requestedBook)
class LibraryDutyAdmin(admin.ModelAdmin):
    form = LibraryDutyForm

admin.site.register(LibraryDuty, LibraryDutyAdmin)
# admin.site.register(Contact)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "event", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
