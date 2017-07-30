import functools
from typing import Optional
from urllib.parse import (
    ParseResult,
    urlparse,
)


@functools.lru_cache()
def parse_url(url) -> Optional[ParseResult]:
    try:
        return urlparse(url)
    except ValueError:
        return None


@functools.lru_cache()
def host_in(url, *hosts):
    parsed = parse_url(url)

    if parsed is None:
        return False

    return parsed.hostname in hosts


@functools.lru_cache()
def get_path(url):
    parsed = parse_url(url)

    if parsed is None:
        return False

    return tuple(parsed.path.split('/'))
