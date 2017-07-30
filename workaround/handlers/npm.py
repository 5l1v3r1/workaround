import requests
import semver

from .base import (
    BaseHandler,
    Workaround,
)

NPM_URL = 'https://registry.npmjs.org/{package}'


class Handler(BaseHandler):
    adjectives = {'released'}

    value_patterns = [
        r'npm:(?P<package>.*) (?P<spec>.*)'
    ]

    example_values = [
        'npm:babel >=2.0',
        'npm:react ~=13.37'
    ]

    def get_result(self, workaround: Workaround, parsed_value):
        npm_package = requests.get(NPM_URL.format(package=parsed_value['package'])).json()
        if any(semver.match(version, parsed_value['spec']) for version in npm_package['versions'].keys()):
            return 'released'

        return 'unreleased'
