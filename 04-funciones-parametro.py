# funcion sin parametro
def nombreFuncion(parametro):
    print("Mensaje")
    nombreFuncion()

#Funcion con parametro
    def nombreFuncionConParametros(parametro):
        print("Este es el parametro:" +parametro) 
        nombreFuncionConParametros("Este es el argumentro del parametro")

#funcion con multiples parametros
def nombreFuncionConMultiplesParametros(parametro1,parametro2):
    print("EStos son los valores de los multiples parametros:"+parametro1,parametro2)
    nombreFuncionConMultiplesParametros("Este es elArgumento1","Este es elArgumento2")