from setuptools import setup, find_packages
import sys, os

version = '0.5.2'

setup(name='pftk',
      version=version,
      description="Python-based open source software framework designed to support portfolio construction and management.",
      long_description=open('README.md').read(),
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Financial and Insurance Industry',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 3',
            'Topic :: Utilities',
      ],
      keywords='finance sharpe portfolio allocation returns',
      author='Charles Gagnon',
      author_email='charlesg@unixrealm.com',
      url='',
      license='New BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            # -*- Extra requirements: -*-
            "numpy >= 1.6.1",
            "scipy >= 0.9.0",
            "matplotlib >= 1.1.0",
            "pandas >= 0.7.3",
            "python-dateutil >= 1.5",
            "scikit-learn >= 0.11",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
