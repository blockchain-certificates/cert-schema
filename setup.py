import os
import re

from setuptools import setup, find_packages

VERSION_FILE = os.path.join('cert_schema', '__version__.py')
__version__ = 'unknown'
try:
    verstrline = open(VERSION_FILE, 'rt').read()
except EnvironmentError as e:
    print('an error occurred', e)
    pass # Okay, there is no version file.
else:
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        __version__ = mo.group(1)
    else:
        print ("unable to find version in %s" % (VERSION_FILE,))
        raise RuntimeError("if %s.py exists, it is required to be well-formed" % (VERSION_FILE,))

here = os.path.abspath(os.path.dirname(__file__))

with open('requirements.txt') as f:
    install_reqs = f.readlines()
    reqs = [str(ir) for ir in install_reqs]

with open(os.path.join(here, 'README.md')) as fp:
    long_description = fp.read()

setup(
    name='cert-schema',
    version=__version__,
    description='Blockchain certificates JSON-LD context and JSON schemas',
    author='info@blockcerts.org',
    url='https://github.com/blockchain-certificates/cert-schema',
    license='MIT',
    author_email='info@blockcerts.org',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={"cert_schema": ["1.1/*.json", "1.2/*.json", "2.0-alpha/*.json", "2.0/*.json", "2.1/*.json", "3.0-alpha/*.json", "3.0-beta/*.json", "3.0/*.json", "3.1/*.json", "3.2/*.json", "context_urls.json"]},
    install_requires=reqs
)
