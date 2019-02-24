import datetime

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .markup import markup


class LiveEntryManager(models.Manager):
    """
    Manager which will only fetch live entries.

    """
    def get_queryset(self):
        return super(
            LiveEntryManager, self).get_queryset().filter(
            status=self.model.LIVE_STATUS
        )


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

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField('Date posted',
                                    default=datetime.datetime.now)
    updated_date = models.DateTimeField(
        blank=True,
        editable=False,
    )
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
        self.updated_date = datetime.datetime.now()
        super(Entry, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('blog_entry_detail',
                (),
                {'year': self.pub_date.strftime('%Y'),
                 'month': self.pub_date.strftime('%b').lower(),
                 'day': self.pub_date.strftime('%d'),
                 'slug': self.slug})


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
        return self.entry_set.filter(status=Entry.LIVE_STATUS)
    live_entries = property(_get_live_entries)
