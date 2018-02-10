from setuptools import setup, find_packages

__version__ = '0.0.2'

setup(
    name='dbusnotify',
    version=__version__,
    description='dbusnotify is a library for creating desktop notifications using the freedesktop.org notification spec',
    long_description='dbusnotify is a library for creating desktop notifications using the freedesktop.org notification spec',
    url='https://github.com/frostidaho/python-dbusnotify',
    download_url='https://github.com/frostidaho/python-dbusnotify/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*', 'examples']),
    include_package_data=True,
    author='Frost Idaho',
    author_email='frostidaho@gmail.com'
)
