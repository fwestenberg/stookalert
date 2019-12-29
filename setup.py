from distutils.core import setup
setup(
  name = 'stookalert',
  packages = ['stookalert'],
  version = '0.2',
  license='MIT',
  description = 'Stookalert package',
  author = 'fwestenberg',
  author_email = '',
  url = 'https://github.com/fwestenberg/stookalert',
  download_url = 'https://github.com/fwestenberg/stookalert/archive/v_02.tar.gz',
  keywords = ['Stookalert', 'Home-Assistant'],
  install_requires=[
          'json',
          'requests',
          'datetime',
          'logging',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
