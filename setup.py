from setuptools import find_packages, setup

import versioneer

with open('requirements.txt') as f:
    requirements = f.read().split()

setup(name='elog',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      license='BSD',
      author='SLAC National Accelerator Laboratory',
      packages=find_packages(),
      description='Utilities for posting to LCLS Experimental ELog',
      scripts=['scripts/LogBookPost.py']
      )
