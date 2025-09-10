def stemmer():
    spørsmål = input("Hvem vil du stemme på?: 0 for høyre, 1 for frp, 2 for venstre, 3 for arbeiderpartiet, 4 for sv, 5 for rødt, 6 for mdg, 7 for krf, 8 for senterpartiet")
    parti = ["høyre", "frp", "venstre", "arbeiderpartiet", "sv", "rødt", "mdg", "krf", "senterpartiet"]
    stemmer_id = [1,2,3,4,5,6,7,8,9]
    # num_of_stemmer = len(stemmer_id)

    stemmning = list(zip(parti,stemmer_id))
    hvilke_stemmer = list(zip(spørsmål, stemmning))
    for spørsmål, stemmer_id in hvilke_stemmer:
        print(spørsmål)

    while True:
        if stemmer_id == []:
            print("Ferdig med å stemme")
            if hvilke_stemmer
            
            # stemme = int("skriv in hvem du vil stemme på: ")
            # if stemme in parti:
            # print("Du har valgt ditt parti")
            # num_of_stemmer.remove()
            # return stemme
        




 # for stemme in parti:
    #     print(stemme)
    #     bruker_stemme = input("Din stemme: ").lower().strip()

    #     if bruker_stemme() == parti.lower():
    #         print("Din stemme har blitt lagret.")
    #         return bruker_stemme