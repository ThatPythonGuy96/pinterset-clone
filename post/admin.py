from django.contrib import admin
from .models import Pin, Tag, Board

@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ('pk', 'profile', 'pin','created', 'description')
    list_filter = ('created', 'profile', 'pin_tag')
    fieldsets = (
        (None, {'fields': ('profile', 'pin', 'description', 'pin_tag')}),
    )
    readonly_fields = ('created',)
    list_per_page = 20

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'pin_count')
    # list_filter = ('created', 'profile',)
    fieldsets = (
        (None, {'fields': ('tag',)}),
    )
    list_per_page = 20

    def pin_count(self, obj):
        return obj.post_tag.count()

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'profile')
    list_filter = ('profile',)
    fieldsets = (
        (None, {'fields': ('name', 'profile', 'pin')}),
    )
    list_per_page = 20