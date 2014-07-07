from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Lyrics
from blog.views import Lyric, LyricDetail, Poem, PoemDetail, Stories, StoryDetail, BlogList, BlogDetail


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^about', 'blog.views.about', name='about'),
    url(r'^lyrics/(?P<pk>\d+)$', LyricDetail.as_view(), name='detail'),
    url(r'^lyrics', Lyric.as_view(), name='listing'),
    url(r'^poems/(?P<pk>\d+)$', PoemDetail.as_view(), name="poem_detail"),
    url(r'^poems', Poem.as_view(), name='poem_listing'),
    url(r'^stories/(?P<pk>\d+)$', StoryDetail.as_view(), name="story_detail"),
    url(r'^stories',Stories.as_view(), name="story_list"),
    url(r'^blog/(?P<pk>\d+)$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^blog', BlogList.as_view(), name="blog_list"),
    
    
   
   
  
   


   )