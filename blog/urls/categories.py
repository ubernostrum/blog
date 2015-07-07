"""
URLs for categories in the blog.

"""

from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$',
        views.CategoryList.as_view(),
        name='blog_category_list'),
    url(r'^(?P<slug>[-\w]+)/$',
        views.CategoryDetail.as_view(),
        name='blog_category_detail'),
]
