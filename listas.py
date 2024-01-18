class Listas:

    def __init__(self, a) -> None:
        self.numero = a
        self.lista = []

    def construirLista(self):
        print(f"Construyendo lista con {self.numero} números.")

        for i in range(self.numero):
            num = int(input(f"Ingrese el número {i + 1}: "))
            self.lista.append(num)
            
    def mostrarLista(self):
        print("La lista construida es:", self.lista)
        
    def ordenarLista(self):
        self.lista.sort()
        print("La lista ordenada es: ", self.lista)
        
    def imprimirNumerosPares(self):
        par = filter(lambda x: x % 2 == 0, self.lista)
        print("Números pares de la lista:", list(par))
        
    def imprimirNumerosImpares(self):
        impar = filter(lambda x: x % 2 != 0, self.lista)
        print("Números impares de la lista:", list(impar))
        
    def imprimirValoresRepetidos(self):
        repeticiones = {}
        for n in self.lista:
            if n in repeticiones :
                repeticiones[n] += 1
            else:
                repeticiones[n] = 0

            resultado={}
            for clave in repeticiones:  
                repeticion = repeticiones[clave]
                if repeticion != 0:
                    resultado[clave] = repeticion + 1
        print("Estos números se repiten en la lista: ",resultado)

def main():
    while True:    
        numeros = int(input("Ingrese la cantidad de números para la lista: "))
        if numeros > 0:
            break
        else:
            print("Por favor, ingrese un número entero positivo.")       

    lista = Listas(numeros)
    lista.construirLista()
    lista.mostrarLista()
    lista.ordenarLista()
    lista.imprimirNumerosPares()
    lista.imprimirNumerosImpares()
    lista.imprimirValoresRepetidos()

if __name__ == "__main__":
    main()
