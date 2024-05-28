from inputs import *
def knapsack(items, b):
    n = len(items)
    dp = [[0 for _ in range(b+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, b+1):
            if items[i-1][0] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1][0]] + items[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]
                
    best_value = dp[n][b]
    best_size = 0
    in_backpack = [0] * n
    current_capacity = b

    for i in range(n, 0, -1):
        if dp[i][current_capacity] != dp[i-1][current_capacity]:
            in_backpack[i-1] = 1
            current_capacity -= items[i-1][0]
            best_size += items[i-1][0]

    return best_value, best_size, in_backpack



def input_():
    print("C for input from console, F for input from file")
    choice = input().strip().upper()
    if choice == "C":
        return input_form_terminal()
    elif choice == "F":
        return input_form_file("input.txt")
    else:
        print("Wrong choice")
        return -1, -1


def main():
    items, b = input_()

    if items == -1 or b == -1:
        return
    value, size, posibility = knapsack(items, b)
    print("Best value:", value)
    print("Best size :", size)
    print("Packed items in best scenario:", posibility)


if __name__ == "__main__":
    main()
