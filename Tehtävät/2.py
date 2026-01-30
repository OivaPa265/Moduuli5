Numero =[]
Luku = input("anna luku")

while Luku != "":

    Numero.append(int(Luku))
    Luku = input("anna luku")

Numero.sort(reverse=True)
for Luku in Numero [:5]:
    print(Luku)