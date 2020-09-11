names = ['Bulbasaur', 'Charmander', 'Squirtle']
hps = [45, 39, 44]

combined_zip = zip(names, hps)
print(type(combined_zip))
print(combined_zip)

combined_zip_list = [*combined_zip]
print(combined_zip_list)
