blog
====

Does what it says on the tin. This is my homegrown blogging app, which
powers `my personal blog <http://www.b-list.org>`_. If you want to see
an example of actually using it, you can check out `the Django project
which powers it <https://github.com/ubernostrum/b_list>`_.

This is essentially the bare-minimum blog application; it has models
for entries and a way to categorize them, some nice text-to-HTML
conversion, and the necessary views and admin bits. I'm pretty happy
with it, and will likely be extremely conservative about adding
features; it's out here in public mainly to serve as a simple example
of:

1. A useful, reusable blog app, and

2. A Django application which runs on both Python 2 and Python 3 (I
   personally deploy to Python 3.3).

However, it's BSD-licensed, so if you want to take it as a baseline
for building your own blog with extra or different features, please
feel free to do so.

