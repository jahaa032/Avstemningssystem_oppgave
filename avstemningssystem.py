import random
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
    stemmer[random_valg] + 1
    print(f"Stemmene er telt og {random_valg} Vant, {weights}")

    return True

def resultat(stemmer):
    print("\n--- Stemme resultat ---")
    for parti, antall in stemmer.items():
        print(f"{parti:.2f}: {antall} stemmer")
        
def vis_prosent(stemmer):
    print("\n--- Stemme resultat ---")
    total = sum(stemmer.values())
    for parti, antall in stemmer.items():
       prosent = (antall / total) * 100
       print(f"{parti}: {prosent:.1f}%")
        # print(f"{parti}: {antall} {prosent} stemmer")


# if stemme.lower() == 'q':
#         print("Hadde")
#         return False

#     if stemme in partier:
#         stemmer[stemme] += 1
#         print(f"Du har stemt på {stemme}!\n")
#     else:
#         print("Du kan ikke stemme på det, prøv igjen.\n")
    
#     return True
        
    # votes = random.choices(random_valg, num_choices)
    # print(f"Valget endte opp med: {votes}")

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

    while True:
        fortsett = falskt_valg(partier, stemmer)
        if not fortsett:
           break

    while resultat <= 169:
        stemmer
        
    resultat(stemmer)

hovedporgram()