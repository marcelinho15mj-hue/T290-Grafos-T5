def get_saturation_degree(graph, v, colors):
    neighbor_colors = set()
    it = iter(graph.adj[v])
    while True:
        try:
            neighbor = next(it)
            if neighbor in colors:
                neighbor_colors.add(colors[neighbor])
        except StopIteration:
            break
    return len(neighbor_colors)

def get_lowest_available_color(graph, v, colors, color_names):
    forbidden_colors = set()
    it = iter(graph.adj[v])
    while True:
        try:
            neighbor = next(it)
            if neighbor in colors:
                forbidden_colors.add(colors[neighbor])
        except StopIteration:
            break
            
    for name in color_names:
        if name not in forbidden_colors:
            return name
    return "Cor Extra"

def dsatur_algorithm(graph):
    color_names = ["Verde", "Amarelo", "Azul", "Branco", "Vermelho", "Roxo", "Laranja", "Rosa", "Cinza", "Preto"]
    colors = {}
    order_of_coloring = []
    uncolored = list(range(graph.V))
    
    while uncolored:
        best_v = None
        max_sat = -1
        max_deg = -1
        
        for v in uncolored:
            sat = get_saturation_degree(graph, v, colors)
            deg = graph.degree(v)
            
            if sat > max_sat:
                max_sat, max_deg, best_v = sat, deg, v
            elif sat == max_sat:
                if deg > max_deg:
                    max_deg, best_v = deg, v
        
        chosen_color = get_lowest_available_color(graph, best_v, colors, color_names)
        colors[best_v] = chosen_color
        order_of_coloring.append(best_v)
        uncolored.remove(best_v)
        
    return colors, order_of_coloring