print("DIAGRAMA DE FLUJO PARA")
print(" RESOLVER PROBLEMAS \n")

print("¿Funciona esta Pendejada?")
print("si")
print("no")

x=str(input("Respuesta:"))

if x=="si":
    print("Ni lo Muevas\n")
    print("No hay Poblema")

elif x=="no":
    print("¿Le moviste Algo?\n")
    print("si")
    print("no")
    
    a=str(input("Respuesta:"))
    
    if a=="si":
        print("¡Pendejo!\n")
        print("¿Sabe alguien que le moviste?")
        print("si")
        print("no")
        c=str(input("Respuesta:"))
        
        if c=="no":
            print("Hazte Pendejo\n")
            print("No hay Problema")
        
        elif c=="si":
            print("¡Ya te Chingaste!\n")
            print("¿Le puedes echar la culpa a Alguien?")
            print("si")
            print("no")
            b=str(input("Respuesta:"))
            
            if b=="si":
                print("No hay Problema")
            while b=="no":
                print("¡Ya te Chingaste!\n")
                print("¿Le puedes echar la culpa a Alguien?")
                print("SI")
                print("NO")
                b=str(input("Respuesta:"))
                if b=="si":
                    print("No hay Problema")
                    break
                    
    elif a=="no":
        print("¿Crees que haya Pedo?\n")
        print("si")
        print("no")
        f=str(input("Respuesta:"))
        
        if f=="si":
            print("¡Ya te Chingaste!\n")
            print("¿Le puedes echar la culpa a Alguien?")
            print("si")
            print("no")
            b=str(input("Respuesta:"))
            
            if b=="si":
                print("No hay Problema")
            while b=="no":
                print("¡Ya te Chingaste!\n")
                print("¿Le puedes echar la culpa a Alguien?")
                print("si")
                print("no")
                b=str(input("Respuesta:"))
                if b=="si":
                    print("No hay Problema")
                    break
                    
        elif f=="no":
            print("Olvidalo\n")
            print("No hay Problema")
        
else:
    print("Responde con un si o con un no :v ")