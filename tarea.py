#Aprobado o reprobado por faltas,adeudos, pago
faltas= int(input("Ingresa las faltas: "))
#faltas=1
if faltas>3:
    print("Reprobado por exceso de faltas")
else:
    #adeudo=4
    adeudo=int(input("Ingresa los adeudos: "))
    if adeudo>3:
        print("Reprobado por adeudo")
    else:
        #pago=true
        pago=bool(input("Ingrese true si tiene adeudo o false si no tiene adeudo: "))
        pago=True
        print("Reprobado por pago")
        pago=False
        print("Aprobado por tener todo al corriente...sigue asi")
