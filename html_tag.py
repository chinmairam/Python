# HTML Tag Function

def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result

x = tag('img', src="Monet.jpg", alt="Sunrise by Claude Monet.", border=1)
print(x)
