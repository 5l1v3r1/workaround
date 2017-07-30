import requests
from packaging.requirements import Requirement
from packaging.utils import canonicalize_name
from packaging.version import parse

from .base import (
    BaseHandler,
    Workaround,
)

PYPI_URL = 'https://pypi.python.org/pypi/{package}/json'


class Handler(BaseHandler):
    adjectives = {'released'}

    value_patterns = [
        'pypi:(?P<value>.*)'
    ]

    example_values = [
        'pypi:Django>=2.0',
        'pypi:colorama~=3.4'
    ]

    def get_result(self, workaround: Workaround, parsed_value):
        requirement = Requirement(parsed_value['value'])
        package_name = canonicalize_name(requirement.name)

        pypi_response = requests.get(PYPI_URL.format(package=package_name)).json()
        releases = list(parse(v) for v in pypi_response['releases'].keys())

        return 'released' if any(requirement.specifier.filter(releases)) else 'unreleased'
