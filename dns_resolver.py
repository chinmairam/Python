import socket
from timeit import timeit

class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache

resolve = Resolver()
print(resolve)
print(resolve('google.com'))
print(resolve.__call__('google.com'))
print(resolve.has_host('google.com'))
#print(resolve.clear())
print(resolve._cache)
print(resolve.__call__('twitter.com'))
print(resolve._cache)
x = timeit(setup="from __main__ import resolve", stmt="resolve('google.com')",
           number=1)
print(x)
# In REPL: print("{:f}".format(_))
