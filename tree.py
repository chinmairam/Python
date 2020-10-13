"""tree = {
    'carnivora': {
        'canis': {
            'c.lupus': 'c.l.familiaris'
        },
        'felis': 'f.catus'
    }
}"""


class Tree(dict):
    def __missing__(self, key):
        value: Tree
        value = self[key] = type(self)()
        return value


tree = Tree()
tree['carnivora']['canis']['c.lupus'] = 'c.l.familiaris'
tree['carnivora']['felis'] = 'f.catus'
print(tree)
