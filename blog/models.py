import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from markdown import markdown
from typogrify.filters import typogrify


def markup(text):
    """
    Mark up plain text into fancy HTML.
    
    """
    return typogrify(markdown(text,
                              lazy_ol=False,
                              output_format='html5',
                              extensions=['abbr',
                                          'codehilite',
                                          'fenced_code',
                                          'sane_lists',
                                          'smart_strong']))


class LiveEntryManager(models.Manager):
    """
    Manager which will only fetch live entries.
    
    """
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)


@python_2_unicode_compatible
class Entry(models.Model):
    """
    An entry in the blog.
    
    """
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )

    author = models.ForeignKey(User)
    pub_date = models.DateTimeField('Date posted',
                                    default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')
    status = models.IntegerField(choices=STATUS_CHOICES,
                                 default=LIVE_STATUS)
    title = models.CharField(max_length=250)

    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True)
    
    excerpt = models.TextField(blank=True, null=True)
    excerpt_html = models.TextField(editable=False, blank=True, null=True)

    categories = models.ManyToManyField('Category')

    live = LiveEntryManager()
    objects = models.Manager()

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ('-pub_date',)
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.body_html = markup(self.body)
        if self.excerpt:
            self.excerpt_html = markup(self.excerpt)
        super(Entry, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('blog_entry_detail',
                (),
                {'year': self.pub_date.strftime('%Y'),
                 'month': self.pub_date.strftime('%b').lower(),
                 'day': self.pub_date.strftime('%d'),
                 'slug': self.slug})

    def _next_previous_helper(self, direction):
        return getattr(self, 'get_%s_by_pub_date' % direction)(status__exact=self.LIVE_STATUS)

    def get_next(self):
        return self._next_previous_helper('next')

    def get_previous(self):
        return self._next_previous_helper('previous')


@python_2_unicode_compatible
class Category(models.Model):
    """
    A category into which entries can be filed.
    
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    description_html = models.TextField(editable=False, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.description_html = markup(self.description)
        super(Category, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('blog_category_detail',
                (),
                {'slug': self.slug})

    def _get_live_entries(self):
        return self.entry_set.filter(status__exact=Entry.LIVE_STATUS)
    live_entries = property(_get_live_entries)
