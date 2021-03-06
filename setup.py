# !/usr/bin/env python

from setuptools import setup, find_packages
import mkdg


def install():
    setup(name=mkdg.__name__,
          description=mkdg.__description__,
          version=mkdg.__version__,
          author=['Kyeongnam Kim'],
          author_email=['devokkn@gmail.com'],
          url=mkdg.__url__,
          download_url=mkdg.__download_url__,
          install_requires=mkdg.__install_requires__,
          license=mkdg.__license__,
          long_description=open('./README.md', 'r', encoding='utf-8').read(),
          packages=find_packages(),
          classifiers=[
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.2',
              'Programming Language :: Python :: 3.3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              'Programming Language :: Python :: 3.7',
              'Programming Language :: Python :: 3.8',
              'Programming Language :: Python :: 3.9',
          ]
          )


if __name__ == "__main__":
    install()
