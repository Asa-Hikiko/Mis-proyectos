print("Diagrama de Flujo de la Ingenieria\n")
print("¿se mueve?\n")
print("si")
print("no")
while "si" or "no" :
    a=str(input("Respuesta:"))
    if a=="si":
        print("¿deberias?\n")
        print("si")
        print("no")
        b=str(input("Respuesta:"))
        if b=="si":
            print("perfecto\n")
            break
        elif b=="no":
            print("usa cinta\n")
            break
    elif a=="no":
        print("¿deberias?\n")
        print("si")
        print("no")
        c=str(input("Respuesta:"))
        if c=="si":
            print("usa WD-40\n")
            break
        elif c=="no":
            print("perfecto\n")
            break
    else:
        print("Respuesta no valida, por favor ingresa 'si' o 'no'.\n")       
    