#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker.
"""
import redis
import requests
from functools import wraps 1 

r = redis.Redis()


def count_url_accesses(method):
    """Decorator to track how many times a URL is accessed."""
    @wraps(method)
    def wrapper(url):
        key = f"count:{url}"
        r.incr(key)
        return method(url)
    return wrapper


@count_url_accesses
def get_page(url: str) -> str:
    """
    Obtains the HTML content of a particular URL and returns it.
    Caches the result with an expiration time of 10 seconds.
    """
    key = f"cache:{url}"
    cached_response = r.get(key)
    if cached_response:
        return cached_response.decode("utf-8")

    response = requests.get(url)
    r.setex(key, 10, response.text)
    return response.text
