from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from tools.models import PersonalityDetails


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ListView.as_view(
    	queryset=PersonalityDetails.objects.all().order_by('name'),
    	template_name="tools/index.html")),
)


