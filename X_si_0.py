#Joc X si 0 cu calculatorul.


from random import randrange

#Initializare tabla:
def afisare_tabla(tabla):
    print("+-----------"*3 + "+")

    for linie in range(3):

        print("|           "*3 + "|")

        x = ""
        for coloana in range(3):

            x += "|    " + str(tabla[linie][coloana]) + "      "
        x+="|"
        print(x)
        print("|           "*3 + "|")
        print("+-----------"*3 + "+")  





# Introducere date user:
def user_casuta(tabla):
    while True:
        nr = int(input("Alege o casuta unde sa pui 0: "))
        if nr < 1 or nr > 9:
            print("Pune 0 in casuta din tabel nu inafara!!!")
            continue

        linie = (nr - 1) // 3
        coloana = (nr - 1) % 3

        if tabla[linie][coloana] in ['X','O']:
            print("Casuta e deja ocupata!")
            continue

        tabla[linie][coloana] = 'O'
        break




#Introducere date program:
def program_casuta(tabla):
    libere = []
    for linie in range(3):
        for coloana in range(3):
            if tabla[linie][coloana] not in ['X','O']:
                libere.append((linie,coloana))

    if len(libere)>0:
        alegere = randrange(len(libere))
        linie , coloana = libere[alegere]
        tabla[linie][coloana] = 'X'




#Functie Victorie:
def victorie(tabla, sgn):
    # linii orizontale
    for linie in range(3):
        if tabla[linie][0] == sgn and tabla[linie][1] == sgn and tabla[linie][2] == sgn:
            return True
    
    # coloane verticale
    for coloana in range(3):
        if tabla[0][coloana] == sgn and tabla[1][coloana] == sgn and tabla[2][coloana] == sgn:
            return True
    
    # diagonala principala (stanga-dreapta)
    if tabla[0][0] == sgn and tabla[1][1] == sgn and tabla[2][2] == sgn:
        return True
    
    # diagonala secundara (dreapta-stanga)
    if tabla[0][2] == sgn and tabla[1][1] == sgn and tabla[2][0] == sgn:
        return True
    
    return False
                


 # Functie Egalitate:       
def egalitate(tabla):
    libere = []
    for linie in range(3):
        for coloana in range(3):
            if tabla[linie][coloana] not in ['X', 'O']:
                libere.append((linie, coloana))
    
    if len(libere) == 0:
        return "Egalitate!"       



tabla = [[3*j + i + 1 for i in range(3)] for j in range(3)]
tabla[1][1] = "X"



while True:
    afisare_tabla(tabla)
    user_casuta(tabla)
    if victorie(tabla, 'O'):
        afisare_tabla(tabla)
        print("Ai castigat!")
        break
    
    program_casuta(tabla)
    if victorie(tabla, 'X'):
        afisare_tabla(tabla)
        print("Am castigat!")
        break
    
    if egalitate(tabla):
        afisare_tabla(tabla)
        print("Egalitate!")
        break
    


