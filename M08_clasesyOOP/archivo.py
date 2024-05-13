class Matematica():
    def __init__(self, lista_numeros):
        self.lista_numeros = lista_numeros
        self.numero = 1

    def verifica_primo(self):
        for i in self.lista_numeros:
            if self.__verifica_primo(i):
                print("El número " + str(i) + " es primo")
            else:
                print("El número " + str(i) + " NO es primo")
            
    def conversion_grados(self):
        lista_gra = ["celsius", "farenheit", "kelvin"]
        for y in self.lista_numeros:
            for i in lista_gra:
                for j in lista_gra:
                    if i != j:
                        print("De " + str(y) + " " + i + " a " + j + " es igual a", self.__conversion_grados(y, i, j))

    def factorial(self):
        for i in self.lista_numeros:
            print("Factorial de " + str(i) + ": " + str(self.__factorial(i)))

    def __verifica_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo
    
    def valor_modal(self, lista):
        lista_unicos = []
        lista_repeticiones = []
        if len(lista) == 0:
            return None
        for elemento in lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
    
    def __conversion_grados(self, valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino

    def __factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            self.numero = numero * self.factorial(numero - 1)
        return self.numero
    