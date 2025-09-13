import random
import json

def lagre_valg(navn, stemmer):
    filnavn = f"{navn}_resultater.json"
    with open(filnavn, "w") as fil:
        json.dump(stemmer, fil, indent=4)
        print(f"Resultatene dine er lagret i {filnavn}")

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


def falskt_valg(partier, stemmer):
    intervaller = [
        (0.31, 0.35),
        (0.14, 0.18),
        (0.27, 0.31),
        (0.053, 0.057),
        (0.053, 0.057),
        (0.017, 0.021),
        (0.041, 0.045),
        (0.047, 0.051),
        (0.053, 0.057),
    ]
    weights = [random.uniform(low, high) for low, high in intervaller]
    random_valg = random.choices(partier, weights=weights, k=1)[0]
    stemmer[random_valg] += 1
    print(f"Stemmene er telt og {random_valg}")

    return True

def resultat(stemmer):
    print("\n--- Stemme resultat ---")
    for parti, antall in stemmer.items():
        print(f"{parti}: {antall} stemmer")
        
def vis_prosent(stemmer):
    print("\n--- Stemme resultat Prosenter ---")
    total = sum(stemmer.values())
    for parti, antall in stemmer.items():
       prosent = (antall / total) * 100
       print(f"{parti}: {prosent:.1f}%")

def hovedporgram():
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

    # while True:
    #     fortsett = falskt_valg(partier, stemmer)
    #     if fortsett <= 40:
    #         return True
    #     elif not fortsett:
    #        break

    for i in range(169):
        falskt_valg(partier, stemmer)
        
        
    resultat(stemmer)
    vis_prosent(stemmer)

    navn = input("Skriv in navnet ditt: ")
    lagre_valg(navn, stemmer)

hovedporgram()