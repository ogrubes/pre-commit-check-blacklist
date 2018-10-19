from setuptools import setup


setup(
    name='check-blacklist',
    description='A pre-commit hook to check for blacklisted files.',
    url='https://github.com/ogrubes/pre-commit-check-blacklist',
    version='1.0.0',

    author='Olivia Grubert',
    author_email='ogrubes@gmail.com',

    packages=[
        'check_blacklist',
    ],
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'check-blacklist = pre_commit_hook.check_blacklist:main',
        ],
    },
)
