from distutils.core import setup


setup(name='blog',
      version='1.3',
      zip_safe=False,  # eggs are the devil.
      description='A blog application for Django.',
      author='James Bennett',
      author_email='james@b-list.org',
      url='https://github.com/ubernostrum/blog/',
      packages=['blog', 'blog.urls', 'blog.templatetags'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Framework :: Django :: 1.7',
                   'Framework :: Django :: 1.8',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Utilities'],
      )
