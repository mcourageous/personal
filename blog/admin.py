from django.contrib import admin
from blog.models import Lyrics, Poems, ShortStory, Blog

class LyricsAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ('title', 'body', 'admin_image')

class PoemAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ('title', 'body', 'admin_image')

class StoryAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ('title', 'body', 'admin_image')

admin.site.register(Lyrics, LyricsAdmin)
admin.site.register(Poems, PoemAdmin)
admin.site.register(ShortStory, StoryAdmin)
admin.site.register(Blog)
