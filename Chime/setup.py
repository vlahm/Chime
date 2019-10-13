from setuptools import setup, find_packages

setup(
    name='chime',

    version='1.0.1',

    description='Set alarms and reminders from terminal',

    long_description = '''Open a terminal window and call chime with the
    number of hours, minutes, and/or seconds to wait before it dings.
    Optionally, set a reminder message.
    e.g.: chime 1h30m "check oven"''',

    url='https://github.com/vlahm/chime',

    author='Mike Vlah',
    author_email='vlahm13@gmail.com',

    license='GPL-3',

    classifiers=[
        
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications :: Gnome',
        'Intended Audience :: End Users/Desktop',
        'Framework :: Setuptools Plugin',
        'Topic :: Desktop Environment :: Gnome',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

    ],

    keywords='desktop, tools, utility, timer',

    packages=find_packages(),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    install_requires=['pyglet'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
  #  entry_points={
  #      'console_scripts': [
  #          'sample=sample:main',
  #      ],
  #  },
)
