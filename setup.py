from distutils.core import setup
setup(
  name = 'stookalert',
  packages = ['stookalert'],
  version = '0.1.1',
  license='MIT',
  description = 'Stookalert package',
  author = 'fwestenberg',
  author_email = '',
  url = 'https://github.com/fwestenberg/stookalert',
  download_url = 'https://github.com/fwestenberg/stookalert/archive/v_011.tar.gz',
  keywords = ['Stookalert', 'Home-Assistant'],
  install_requires=[
          'requests',
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
