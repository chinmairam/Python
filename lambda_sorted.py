scientists = ['Marie Curie', 'Albert Einstein', 'Issac Newton',
              'Charles Darwin']
x = sorted(scientists, key=lambda name:name.split()[-1])
print(x)
