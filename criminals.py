import json

def criminals(most_wanted, new_criminals):
    """
    ve funkci kontrolujeme, jeslit se nekdo z novych nenachazi v seznamu starych
    :param most_wanted: spucasny seznam zlocincu
    :param new_criminals: novy slovnik zlocincu
    :return:aktualizovany slovnik most_wanted
    """

    for zlocinec in new_criminals:
        most_wanted[zlocinec] = new_criminals[zlocinec]

    return most_wanted


def get_production(nazev_statu, origin, most_wanted):
    """
    vyplivne celkovou produkci drog pro dany stat za posledni tri roky
    :param nazev_statu: (string) pro ktery stat to chceme vedet
    :param slovnik_origin: slovnik radici zlocince jako mnozinu ke statum jako klici
    :param slovnik_most_wanted: slovnik  zlocince a jeho drogove produkce
    :return: int - celkova produkce za posledni tri roky
    """
#ziskam mnozinu vsech zlocincu z daneho statu
    padousi = origin[nazev_statu]
    sum = 0
    for padouch in padousi:
        seznam_produkci = most_wanted[padouch]
        suma = seznam_produkci[0] + seznam_produkci[1] + seznam_produkci[2]
        sum = sum + suma
    return sum

def main ():
    names = ["Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"]
    production = [(138, 164, 151), (125, 113, 113), (52, 50, 63)]
    most_wanted = dict(zip(names, production))

    with open("new_criminals.json", mode="r") as json_file:
        new_criminals = json.load(json_file)


#hlavni funkci rozsirim os lovnik origin, ktery vyjadruje puvod zlocincu
    origin = {
        "Mexico": {"Manuel Noriega", "Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"},
        "Columbia": {"Rick Ross", "William Jardine"},
    }

    return new_criminals, criminals(most_wanted, new_criminals), get_production("Mexico", origin, most_wanted)
print(main())



