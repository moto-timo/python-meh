#!/usr/bin/python3

from distutils.core import setup

setup(name='python-meh', version='0.50.1',
      description='Python module for handling exceptions',
      author='Chris Lumens', author_email='clumens@redhat.com',
      url='http://git.fedoraproject.org/git/?p=python-meh.git',
      data_files = [('/usr/share/python-meh', ['ui/exception-dialog.glade'])],
      packages=['meh', 'meh.ui'])
