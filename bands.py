bands = list()

with open('bands.txt') as f:
    for line in f:
        bands.append(line.strip())

bands.sort()
print(bands)

with open('bands.txt', 'w') as f:
    for band in bands:
        f.write(band + '\n')
