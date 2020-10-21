class Sample:
    def __init__(self):
        self.x = 5
    def change(self):
        self.x = 10

class Derived_sample(Sample):
    def change(self):
        self.x=self.x+1
        return self.x

def main():
    obj = Derived_sample()
    print(obj.change())

main()
