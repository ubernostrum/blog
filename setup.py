from distutils.core import setup
import os


setup(name='blog',
      version='1.0',
      description='A blog application for Django.',
      author='James Bennett',
      author_email='james@b-list.org',
      url='http://bitbucket.org/ubernostrum/blog/overview/',
      download_url='http://bitbucket.org/ubernostrum/blog/downloads/blog-1.0.tar.gz', 
      packages=['blog', 'blog.templatetags'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Topic :: Utilities'],
      )
