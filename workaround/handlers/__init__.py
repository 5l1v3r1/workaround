import pkg_resources
from functools import lru_cache
from .base import BaseHandler
from typing import Dict


@lru_cache(None)
def get_handlers() -> Dict[str, BaseHandler]:
    return {
        entry.name: entry.load()()
        for entry in
        pkg_resources.iter_entry_points('workaround_handlers')
    }


@lru_cache(None)
def get_all_adjectives():
    return {
        adjective
        for handler in get_handlers().values()
        for adjective in handler.adjectives
    }


@lru_cache()
def get_handler(value, adjective):
    handlers = get_handlers()

    for handler in handlers.values():
        if handler.can_handle(value, adjective):
            return handler
