from django.contrib import admin
from tools.models import PersonalityDetails

class PersonalityAdmin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['name', 'title', 'date',]

admin.site.register(PersonalityDetails, PersonalityAdmin)


