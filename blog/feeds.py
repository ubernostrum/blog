from django.utils.feedgenerator import Atom1Feed

from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed

from .models import Category
from .models import Entry


current_site = Site.objects.get_current()


class EntriesFeed(Feed):
    author_name = "James Bennett"
    copyright = "http://www.b-list.org/about/copyright/"
    description = "Latest entries posted to %s" % current_site.name
    feed_type = Atom1Feed
    item_copyright = "http://www.b-list.org/about/copyright/"
    item_author_name = "James Bennett"
    item_author_link = "http://www.b-list.org/"
    link = "/feeds/entries/"
    title = "%s: Latest entries" % current_site.name

    description_template = 'feeds/entry_description.html'
    title_template = 'feeds/entry_title.html'

    def item_categories(self, item):
        return [c.title for c in item.categories.all()]

    def item_guid(self, item):
        return "tag:%s,%s:%s" % (current_site.domain,
                                 item.pub_date.strftime('%Y-%m-%d'),
                                 item.get_absolute_url())

    def item_pubdate(self, item):
        return item.pub_date

    def item_updateddate(self, item):
        return item.updated_date

    def items(self):
        return Entry.live.all()[:15]


class CategoryFeed(EntriesFeed):
    def description(self, obj):
        return "%s: Latest entries in category '%s'" % (current_site.name,
                                                        obj.title)

    def get_object(self, request, slug):
        return Category.objects.get(slug=slug)

    def items(self, obj):
        return obj.live_entries[:15]

    def link(self, obj):
        return obj.get_absolute_url()

    def title(self, obj):
        return "%s: Latest entries in category '%s'" % (current_site.name,
                                                        obj.title)
