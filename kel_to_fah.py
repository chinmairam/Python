def kel_to_fah(temp):
    assert (temp >= 0),"Colder than absolute zero!"
    return ((temp-273)*1.8)+32

print(kel_to_fah(273))
print(int(kel_to_fah(505.78)))
print(kel_to_fah(-5))
