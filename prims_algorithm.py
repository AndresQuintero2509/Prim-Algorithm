""" Implementacion del algoritmo de Prim """
class Prim():
    """ Implementacion del algoritmo de Prim """

    def __init__(self):
        """ Constructor """
        self.conexiones = [[1, 3, 6],
                           [2, 3, 7, 8, 9],
                           [3, 5, 10],
                           [2, 7, 8],
                           [1, 4, 5, 9],
                           [2, 5, 7, 8]]
        self.matriz_arcos = []

    def algoritmo_prim(self):
        """ Orquesta la ejecucción del algoritmo de Prim """
        i = len(self.conexiones)
        for j in range(i):
            if not j == i-1:
                lista1 = []
                lista2 = []
                match = []
                contador_match1 = 0
                contador_match2 = 0
                n = 0
                m = 0
                elementos = len(self.conexiones[j])
                for k in range(elementos):
                    valor = self.conexiones[j][k]
                    lista1 = self.conexiones[j]
                    lista2 = self.conexiones[j+1]
                    if valor in self.conexiones[j] and valor in self.conexiones[j+1]:
                        match.append(valor)
                for item in lista1:
                    if item in match and item in lista1:
                        contador_match1 += 1
                for item in lista2:
                    if item in match and item in lista2:
                        contador_match2 += 1
                m = len(lista2) + len(lista1) - contador_match1 - contador_match2
                n = len(match)
                disparidad = 1 - (n/(n+m))
                self.matriz_arcos.append([j+1, j+2, disparidad])
            else:
                self.print_matriz()
                break

    def print_matriz(self):
        """ Imprime la matriz de arcos y pesos """
        print(f'Matriz de arcos y pesos')
        for elemento in self.matriz_arcos:
            print(elemento)

if __name__ == "__main__":
    Prim().algoritmo_prim()
