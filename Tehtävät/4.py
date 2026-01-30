kaupunki =[]
nmr=2
print("anna viisi kaupunkia jos annat tyhjän  vastauksen ohjelmisto printaa annetun määrän")
syote = input(f"anna ensimäinen kaupunki")
while syote != "":

    kaupunki.append(syote)

    if nmr == 6:
        break

    syote = input(f"anna kaupunki numero {nmr}")
    nmr= nmr+1

print("kaupungit annetussa järjestyksessä")
for i in kaupunki:
    print(i)