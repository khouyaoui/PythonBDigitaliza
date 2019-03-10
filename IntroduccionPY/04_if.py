print("Control de programas de una discoteca a través de la edad")
edad=int(input("Cuantos años tienes?\n"))

if (edad<=20):
    if(edad<18):
        print("Tu edad es "+str(edad)+". No hay programas para ti. :(")
    else:
        print("Tu edad es " +str(edad)+" Hay programas para ti en la sala 21.")

if ((edad>20)&(edad<=39)):
    print("Tu edad es "+str(edad)+" Hay programas para ti en la sala 25.")

if ((edad>=40)&(edad<=59)):
    print("Tu edad es "+str(edad)+" Hay programas para ti en la sala S2.")

if(edad>=60):
    print("Tu edad es "+str(edad)+". Hoy No hay programas para ti. :(")