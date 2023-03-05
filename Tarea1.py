#Aprobado o reprobado por faltas,adeudos
faltas= int(input("Ingresa las faltas: "))
if faltas>3:
    print(f'REPROBADO POR: {faltas} FALTAS')
else:
    pago=int(input("Ingresa los adeudos: "))
    if pago>3:
        print(f'REPROBADO POR UN TOTAL DE:{pago} ADEUDOS')
    else:
        rep=faltas+pago
        if rep<3:
            print('APROBADO')
            print(f'CUIDA TUS FALTA(S): {faltas}'
           f' Y ADEUDO(S): {pago}',
            f'POR QUE FUERON EN TOTAL: {rep} FALTA(S)')
        else:
            print('REPROBADO')
            print(f'POR {faltas} FALTA(S)'
            f' Y {pago} ADEUDO(S) QUE',
            f'DIERON UN TOTAL DE: {rep} FALTAS')
        



   

  
        
   

   
   
    


  
 
