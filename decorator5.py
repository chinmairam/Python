# Converts non-ascii to ascii.
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

def northern_city():
    return 'TromΦ'

print(northern_city())

@escape_unicode
def northern_city():
    return 'TromΦ' # Use Alt+1000 to type phi.

print(northern_city())
