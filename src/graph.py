from algs4.bag import Bag

class Graph:
    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adj = [Bag() for _ in range(self.V)]

    def __str__(self):
        lines = ["%d vertices, %d edges" % (self.V, self.E)]
        for v in range(self.V):
            neighbors_list = []
            it = iter(self.adj[v])
            while True:
                try:
                    w = next(it)
                    neighbors_list.append(str(w))
                except StopIteration:
                    break
            lines.append("%d: %s" % (v, " ".join(neighbors_list)))
        return "\n".join(lines)

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1

    def degree(self, v):
        return self.adj[v].size()

    def max_degree(self):
        max_deg = 0
        for v in range(self.V):
            max_deg = max(max_deg, self.degree(v))
        return max_deg

    def number_of_self_loops(self):
        count = 0
        for v in range(self.V):
            it = iter(self.adj[v])
            while True:
                try:
                    w = next(it)
                    if w == v:
                        count += 1
                except StopIteration:
                    break
        return count // 2


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python graph.py <arquivo.txt>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            
            if not lines:
                print("Arquivo vazio.")
                sys.exit(1)

            V = int(lines[0])
            E = int(lines[1])
            g = Graph(V)
            
            for i in range(2, 2 + E):
                parts = lines[i].split()
                if len(parts) >= 2:
                    v, w = parts[0], parts[1]
                    g.add_edge(v, w)
            
            print(g)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{sys.argv[1]}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o grafo: {e}")