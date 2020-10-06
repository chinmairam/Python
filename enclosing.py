message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        global message # changes scope from global into another. 
        message = 'local'


    print('enclosing message:', message)
    local()
    print('enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)
