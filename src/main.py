import sys
import os

# Ajuste de path para localizar os módulos na pasta src
sys.path.append(os.path.dirname(__file__))

from graph import Graph
from dsatur import dsatur_algorithm

def validate_coloring(graph, colors):
    for v in range(graph.V):
        it = iter(graph.adj[v])
        while True:
            try:
                neighbor = next(it)
                if colors[v] == colors[neighbor]:
                    return False
            except StopIteration:
                break
    return True

def main():
    # Mapeamento oficial exigido pelo enunciado
    mapeamento = {
        0:"AC", 1:"AL", 2:"AM", 3:"AP", 4:"BA", 5:"CE", 6:"DF", 7:"ES", 8:"GO", 9:"MA",
        10:"MG", 11:"MS", 12:"MT", 13:"PA", 14:"PB", 15:"PE", 16:"PI", 17:"PR", 18:"RJ",
        19:"RN", 20:"RO", 21:"RR", 22:"RS", 23:"SC", 24:"SE", 25:"SP", 26:"TO"
    }

    if len(sys.argv) < 2:
        print("Uso: python src/main.py dados/brasil.txt")
        return

    try:
        with open(sys.argv[1], 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            if not lines: return
            
            V_count = int(lines[0])
            E_count = int(lines[1])
            g = Graph(V_count)
            
            # Lê apenas a quantidade de arestas especificada no cabeçalho
            for i in range(2, 2 + E_count):
                v, w = lines[i].split()
                g.add_edge(v, w)
    except Exception as e:
        print(f"Erro ao processar o ficheiro: {e}")
        return

    print("--- LISTA DE ADJACÊNCIA (ESTADOS) ---")
    # Imprime a lista de adjacência usando as siglas
    for v in range(g.V):
        vizinhos = []
        it = iter(g.adj[v])
        while True:
            try:
                n = next(it)
                vizinhos.append(mapeamento[n])
            except StopIteration:
                break
        print(f"{mapeamento[v]}: {' '.join(vizinhos)}")

    # Executa o DSatur
    colors, order = dsatur_algorithm(g)
    
    unique_colors_used = set(colors.values())
    total_count = len(unique_colors_used)

    print("\n--- ORDEM DE COLORAÇÃO (DSatur) ---")
    print(" -> ".join([mapeamento[v] for v in order]))

    print("\n--- CORES ATRIBUÍDAS POR ESTADO ---")
    for v in sorted(colors.keys()):
        print(f"{mapeamento[v]}: {colors[v]}")

    print(f"\nTotal de cores utilizadas: {total_count} ({', '.join(sorted(unique_colors_used))})")
    
    if validate_coloring(g, colors):
        print("A coloração produzida é válida? Sim")
    else:
        print("A coloração produzida é válida? Não")

if __name__ == "__main__":
    main()