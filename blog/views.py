from django.shortcuts import render
from blog.models import Lyrics, Poems, ShortStory, Blog
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse

def home(request):
	return render(request, 'blog/base.html')


def about(request):
	return render(request, 'blog/about.html')

class Lyric(ListView):
	model = Lyrics

class LyricDetail(DetailView):
	model = Lyrics
	template_name = "blog/lyric_detail.html"

	def get_context_data(self, **kwargs):
		context =super(LyricDetail, self).get_context_data(**kwargs)
		context['lyric'] = Lyrics.objects.get(pk=self.kwargs.get('pk', None))
		return context




class Poem(ListView):
	model = Poems
	template_name="blog/poem_list.html"

class PoemDetail(DetailView):
	model = Poems
	template_name="blog/poem_detail.html"

	def get_context_data(self, **kwargs):
		context = super(PoemDetail, self).get_context_data(**kwargs)
		context['p'] = Poems.objects.get(pk=self.kwargs.get('pk', None))
		return context



class Stories(ListView):
	model = ShortStory
	template_name="blog/stories_list.html"

class StoryDetail(DetailView):
	model = ShortStory
	template_name="blog/stories_detail.html"


	def get_context_data(self, **kwargs):
		context = super(StoryDetail, self).get_context_data(**kwargs)
		context['st'] = ShortStory.objects.get(pk=self.kwargs.get('pk', None))
		return context


class BlogList(ListView):
	model = Blog
	template_name="blog/blog_list.html"


class BlogDetail(DetailView):
	model = Blog
	template_name="blog/blog_detail.html"


	def get_context_data(self, **kwargs):
		context = super(BlogDetail, self).get_context_data(**kwargs)
		context['bl'] = Blog.objects.get(pk=self.kwargs.get('pk', None))
		return context

	



# def lyrics_page(request):
# 	lyrics = Lyrics.objects.all()
# 	return render(request, 'tools/lyrics.html', {'lyrics':lyrics})

# def poems_page(request):
# 	poems = Poems.objects.all()
# 	return render(request, 'tools/poems.html', {'poems':poems})

# def short_story(request):
# 	stories = ShortStory.objects.all()
# 	return render(request, 'tools/stories.html', {'stories':stories})
