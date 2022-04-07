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


def main ():
    names = ["Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"]
    production = [(138, 164, 151), (125, 113, 113), (52, 50, 63)]
    most_wanted = dict(zip(names, production))

    with open("new_criminals.json", mode="r") as json_file:
        new_criminals = json.load(json_file)

    return new_criminals, "\n", criminals(most_wanted, new_criminals)
print(main())



