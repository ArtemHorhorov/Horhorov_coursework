
from django.contrib import admin
from .models import Event, Location, User, Assignment, Comment, Tag

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'user_count')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'description')
    date_hierarchy = 'start_date'

    @admin.display(description='Количество пользователей')
    def user_count(self, obj):
        return obj.users.count()

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'event')
    list_filter = ('event', 'due_date')
    search_fields = ('title',)
    raw_id_fields = ('event',)
    filter_horizontal = ('tags',)
 
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1

class LocationInline(admin.TabularInline):
    model = Location
    extra = 1

class CommentAdmin(admin.ModelAdmin):
    list_display = ('location', 'user', 'created_at')
    list_filter = ('location', 'user')
    readonly_fields = ('created_at',)

admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Assignment)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)