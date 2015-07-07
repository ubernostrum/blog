"""
URLs for entries in the blog.

"""

from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^$',
        views.EntryArchiveIndex.as_view(),
        name='blog_entry_archive_index'),
    url(r'^(?P<year>\d{4})/$',
        views.EntryArchiveYear.as_view(),
        name='blog_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
        views.EntryArchiveMonth.as_view(),
        name='blog_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
        views.EntryArchiveDay.as_view(),
        name='blog_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        views.EntryDetail.as_view(),
        name='blog_entry_detail'),
]
