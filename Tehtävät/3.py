Syote= int(input("mikä  numero?"))
vastaus = False

for i in range(2, Syote):
    if Syote % i  ==0:
        vastaus=True
        break

if vastaus:
    print(f"{Syote} ei ole alku luku")
else:
    print(f"{Syote} on alku luku")