import random
def GrafGen(n):
    with open("zad3/inputIN.txt", "w") as file:
        file.write(str(n) + " " + str(int(n*(n-1)/2*1/2)) + "\n")
        pairs = set()
        i = 0
        while i < int(n*(n-1)/2*1/2):
            a = random.randint(0,n-1)
            b = random.randint(0,n-1)
            if a != b and (a,b) not in pairs and (b,a) not in pairs:
                file.write(str(a) + " " + str(b) + "\n")
                i += 1
                pairs.add((a,b))
                pairs.add((b,a))
    return
if __name__ == "__main__":
    GrafGen(10)