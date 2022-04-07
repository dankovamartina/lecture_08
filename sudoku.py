import numpy as np

def main():
    assert is_correct([1, 2, 8, 9, 3, 5, 6, 7, 4]) == True
    assert is_correct([1, 2, 8, 9, 3, 5, 7, 4]) == False
    assert is_correct([1, 1, 2, 8, 9, 3, 5, 7, 4]) == False
    assert is_correct([]) == False

    return is_correct([1, 2, 6, 8, 9, 3, 5, 7, 11])

def is_correct(seznam):
    """
    funkce zkontroluje, zda radek - senzma cisel obsahuje kazde cislo prave jednou
    :param seznam: seznam s deviti cisly
    :return: (bool) True pokud je radek spravne vyplnen, False pokud je vyplnen spatne
    """
    pole = np.array(seznam)
    if len(set(seznam)) == 9 and np.sum(pole) ==  45:
        return True
    else:
        return False

if __name__ == "__main__":
    print(main())

