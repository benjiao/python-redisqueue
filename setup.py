"""
python-redisqueue
"""
from setuptools import setup

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

setup(
    name='redisqueue',
    version='0.1.0a1',
    url='http://code.benjie.me/python-redisqueue',
    license='BSD',
    author='Benjie Jiao',
    author_email='benjiao12@gmail.com',
    description='An easy to use redis-based queue implementation',
    long_description=long_description,
    py_modules=['redisqueue.redisqueue'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['redis'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
