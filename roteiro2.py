from grafo import Grafo

def grafoToMatriz(g: Grafo): 
    
    matriz = []
    for i in range(len(g.N)):
        matriz.append([])
    
    

def vertices_nao_adjacentes(g: Grafo):    

    return

def ha_laco(g: Grafo):

    return

def ha_paralelas(g: Grafo):
    
    return

def grau(g: Grafo, vetice):

    return

def arestas_sobre_vertice(g: Grafo, vetice):

    return

def eh_completo(g: Grafo):

    return

def conexo(g: Grafo):

    return 
pass

def main():

    g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})
    grafoToMatriz(g_p)

    
main()