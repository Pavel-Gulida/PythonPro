import functools
import sys
import tracemalloc

import requests


def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._frequency[cache_key] += 1
                return deco._cache[cache_key]

            # видаляємо якшо досягли ліміта
            if len(deco._cache) >= max_limit:
                min_f = min(deco._frequency.values())
                for key, el in deco._frequency.items():
                    if el == min_f:
                        deco._cache.pop(key)
                        deco._frequency.pop(key)
                        break

            result = f(*args, **kwargs)
            deco._cache[cache_key] = result
            deco._frequency[cache_key] = 1
            return result

        deco._cache = dict()
        deco._frequency = dict()
        return deco

    return internal


def size_memory(f):
    def deco(*args, **kwargs):
        tracemalloc.start()
        result = f(*args, **kwargs)
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')
        for stat in top_stats:
            print(stat)
        print("-"*150)
        return result

    return deco


@cache()
@size_memory
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


print(fetch_url('https://google.com'))
