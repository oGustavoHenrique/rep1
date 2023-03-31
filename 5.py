def inverter(string):
    inversa = ""
    for i in range(len(string)-1, -1, -1):
        inversa += string[i]
    return inversa

string = str(input("string: "))
print(inverter(string))

