def vis_partier(partier):
    print("Du kan stemme på disse partiende: ")
    for parti in partier:
        print(f"- {parti}")

def sjekk_stemmer(partier, stemmer):
    stemme = input("Hvilket parti vil du stemme på?(eller 'q' for å avslutte): ")

    if stemme.lower() == 'q':
        print("Hadde")
        return False

    if stemme in partier:
        stemmer[stemme] += 1
        print(f"Du har stemt på {stemme}!\n")
    else:
        print("Du kan ikke stemme på det, prøv igjen.\n")
    
    return True

def resultat(stemmer):
    print("\n--- Stemme resultat ---")
    for parti, antall in stemmer.items():
        print(f"{parti}: {antall} stemmer")
    
def hovedprgram():
    partier = [
        "ap",
        "høyre",
        "frp",
        "sp",
        "sv",
        "venstre",
        "krf",
        "mdg",
        "rødt",
    ]
    stemmer = {parti: 0 for parti in partier}

    print("Velkomen til valget")
    vis_partier(partier)

    while True:
        fortsett = sjekk_stemmer(partier, stemmer)
        if not fortsett:
            break

    resultat(stemmer)

hovedprgram()




# print("Disse er partiende du kan stemme på: ")
# for p in partier:
#     print("-", p)

# while True:
#     stemme = input("Hvem vil du stemme på av partiende?: ").strip().lower()

#     if stemme in p:
#         partier[stemme] += 1
#         print(f"Du stemte på {stemme}")
#     else:
#         print("Du kan ikke stemme på det, prøv igjen.")






# def stemmer():
#     spørsmål = input("Hvem vil du stemme på?: 0 for høyre, 1 for frp, 2 for venstre, 3 for arbeiderpartiet, 4 for sv, 5 for rødt, 6 for mdg, 7 for krf, 8 for senterpartiet")
#     parti = ["høyre", "frp", "venstre", "arbeiderpartiet", "sv", "rødt", "mdg", "krf", "senterpartiet"]
#     stemmer_id = [1,2,3,4,5,6,7,8,9]
#     # num_of_stemmer = len(stemmer_id)

#     stemmning = list(zip(parti,stemmer_id))
#     hvilke_stemmer = list(zip(spørsmål, stemmning))
#     for spørsmål, stemmer_id in hvilke_stemmer:
#         print(spørsmål)

#     while True:
#         if stemmer_id == []:
#             print("Ferdig med å stemme")
#             if hvilke_stemmer
            
#             # stemme = int("skriv in hvem du vil stemme på: ")
#             # if stemme in parti:
#             # print("Du har valgt ditt parti")
#             # num_of_stemmer.remove()
#             # return stemme
        




#  # for stemme in parti:
#     #     print(stemme)
#     #     bruker_stemme = input("Din stemme: ").lower().strip()

#     #     if bruker_stemme() == parti.lower():
#     #         print("Din stemme har blitt lagret.")
#     #         return bruker_stemme