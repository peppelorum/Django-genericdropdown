from setuptools import setup, find_packages

setup(
    name='django-genericdropdown',
    version=0.1,
    description='A simple dropdown the make the hassle of picking to the right object when using generic relations',
    long_description=open('readme.markdown', 'r').read(),
    keywords='django, admin, dropdown',
    author='Peppe Bergqvist',
    author_email='p at bergqvi st',
    url='https://github.com/peppelorum/Django-genericdropdown',
    license='Beer License',
    package_dir={'genericdropdown': 'genericdropdown'},
    package_data={'genericdropdown': ['templates/admin/treenav/menuitem/*.html']},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Communications",
        ],
    zip_safe=False,
    )
