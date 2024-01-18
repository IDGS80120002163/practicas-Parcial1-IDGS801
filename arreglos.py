class Arreglos:

    #Declaracion de métodos
    def __init__(self, a) -> None:
        self.numero = a

    #Método para construir la pirámide de asteríscos
    def construirPiramide(self):
        print("Pirámide de asteríscos hasta el número", self.numero)
        
        #Con el ciclo for se imprime el asterísco según el número que siga en el ciclo
        for i in range(1, self.numero + 1):
            print('*' * i)

def main():
    
    piramide = int(input("Dame un número: "))
    obj = Arreglos(piramide)
    obj.construirPiramide()

if __name__ == "__main__":
    main()
