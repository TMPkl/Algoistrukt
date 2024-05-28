def input_form_terminal():
    try: 
        n,b = [float(x) for x in input().split()]                                       #(liczba przedmiotów, pojemność plecaka),######################################################################################
        n = int(n)
    except ValueError:
        print("Zła liczba argumentów")
    if n < 1 or b < 1:
        print("Złe dane wejściowe:- liczba przedmiotów lub pojemność plecaka mniejsza od 1")
        return -1, -1
    #kolejne wiersze to pary liczb r w (rozmiar przedmiotu, wartość przedmiotu).
    items = []
    for i in range(n):
        try:
            r,w = [float(x) for x in input().split()] ######################################################################################
            if r < 0 or w < 0:
                print("Złe dane wejściowe:- rozmiar przedmiotu lub wartość przedmiotu mniejsza od 0")
                return -1, -1
            items.append((r,w))
        except ValueError:
            print("Zła liczba argumentów")
            return -1, -1
    return items, b

def input_form_file(file):
    try:
        with open(file, "r") as f:
            n,b = [int(x) for x in f.readline().split()] #############                                      #(liczba przedmiotów, pojemność plecaka),\
            if n < 1 or b < 1:
                print("Złe dane wejściowe:- liczba przedmiotów lub pojemność plecaka mniejsza od 1")
                return -1, -1
            items = []
            for i in range(n):
                r,w = [int(x) for x in f.readline().split()] ############################################################################################################
                if r < 0 or w < 0:
                    print("Złe dane wejściowe:- rozmiar przedmiotu lub wartość przedmiotu mniejsza od 0")
                    return -1, -1
                items.append((r,w))
            return items, b
    except FileNotFoundError:
        print("Nie znaleziono pliku")
        return -1, -1
    