def creer_plateau():
    plateau = [[" " for _ in range(8)] for _ in range(8)]
    for i in range(3): 
        for j in range(8):
            if (i + j) % 2 == 1:
                plateau[i][j] = "x"
    for i in range(5, 8):  
        for j in range(8):
            if (i + j) % 2 == 1:
                plateau[i][j] = "o"
    return plateau

def afficher_plateau(plateau):
    print("   " + " ".join(str(j) for j in range(8)))
    for i in range(8):
        print(i, " ".join(plateau[i]))