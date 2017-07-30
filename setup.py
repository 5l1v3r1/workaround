from setuptools import setup

setup(
    name='workaround',
    version='0.1',
    packages=['workaround'],
    url='',
    license='',
    author='Tom Forbes',
    author_email='tom@tomforb.es',
    description='',
    install_requires=[
        'requests',
        'docopt',
        'colorama',
        'termcolor',
        'requests',
        'packaging',
        'semver',
        'regex'
    ],
    entry_points={
        'console_scripts': [
            'workaround = workaround.cli:run'
        ],
        'workaround_handlers': [
            'github = workaround.handlers.github:Handler',
            'pypi = workaround.handlers.pypi:Handler',
            'django = workaround.handlers.django:Handler',
            'npm = workaround.handlers.npm:Handler'
        ]
    }
)
