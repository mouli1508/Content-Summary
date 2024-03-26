import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'Content-Summary'
AUTHOUR_USER_NAME = 'mouli1508'
SRC_REPO = 'contentSummarizer'
AUTHOR_EMAIL = 'cprabhak@kent.edu'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOUR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Python application for summarizing content',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOUR_USER_NAME}/{SRC_REPO}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOUR_USER_NAME}/{SRC_REPO}/issues',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)