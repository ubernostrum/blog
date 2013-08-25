"""
URLs for the blog's feeds.

"""

from django.conf.urls import patterns
from django.conf.urls import url

from blog.feeds import CategoryFeed
from blog.feeds import EntriesFeed


urlpatterns = patterns('',
                       url(r'^entries/$',
                           EntriesFeed(),
                           name='blog_feeds_entries'),
                       url(r'^categories/(?P<slug>[-\w]+)/$',
                           CategoryFeed(),
                           name='blog_feeds_category'),
)
