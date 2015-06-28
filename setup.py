"""
python-redisqueue
"""
from setuptools import setup

setup(
    name='python-redisqueue',
    keywords=['redis queue'],
    version='1.0.2',
    url='http://code.benjie.me/python-redisqueue',
    license='BSD',
    author='Benjie Jiao',
    author_email='benjiao12@gmail.com',
    description='An easy to use redis-based queue implementation',
    long_description='An easy to use redis-based queue implementation',
    py_modules=['python_redisqueue.python_redisqueue'],
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
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
