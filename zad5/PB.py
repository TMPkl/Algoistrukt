from inputs import *
import itertools as it 

def all_posibilities(n):
    return list(it.product(range(2), repeat=n))

def calculate_value(items, posibility):
    value = 0
    for i in range(len(items)):
        value += items[i][1] * posibility[i]
    return value

def calculate_size(items, posibility):
    size = 0
    for i in range(len(items)):
        size += items[i][0] * posibility[i]
    return size

def knapsack(items, b):
    best_value = 0
    best_size = 0
    best_posibility = []
    for posibility in all_posibilities(len(items)):
        value = calculate_value(items, posibility)
        size = calculate_size(items, posibility)
        if size <= b and value > best_value:
            best_value = value
            best_size = size
            best_posibility = posibility
    return best_value, best_size, best_posibility

def main():
    print("C for input form console, F for input from file")
    choice = input()
    if choice == "C":
        items, b = input_form_terminal()
    elif choice == "F":
        items, b = input_form_file("input.txt")
    else:
        print("Wrong choice")
        return
    if items == -1 or b == -1:
        return
    value, size, posibility = knapsack(items, b)
    print("Best value:", value)
    print("Best size :", size)
    print("Packed items in best scenario:", posibility)

if __name__ == "__main__":
    main()