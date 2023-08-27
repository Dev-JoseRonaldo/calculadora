import sys
import read_data

#classe responsável por representar um grafo
class Graph(object):
    #construtuor
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    #método responável por retornar os nos do grafo
    def get_nodes(self):
        return self.nodes
    
    #método responsável por retornar as nós vizinhos (conectados por arestas)
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    #método responsável por retornar o peso da aresta entre dois nós
    def value(self, node1, node2):
        return self.graph[node1][node2]
    
def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    #dicionário responsável por atualizar o menor caminho ao avançar no grafo
    shortest_path = {}
 
    #salva o caminho mais curto até o momento
    previous_nodes = {}
 
    #valor muito grande usado para iniciar o valor de menor caminho  
    max_value = sys.maxsize
    #adiciona esse valor em todos os nós
    for node in unvisited_nodes:
        shortest_path[node] = max_value

    #caminho do nó inicia é iniciado como 0   
    shortest_path[start_node] = 0
    
    #loop responsável por visitar todos os nós do grafo
    while unvisited_nodes:
        
        current_min_node = None
        #loop que itera todos os nós
        for node in unvisited_nodes:
            #Encontra o nó com o peso mais baixo
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # atualiza as distancias do nós vizinhos do nó atual
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            temp_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if temp_value < shortest_path[neighbor]:
                shortest_path[neighbor] = temp_value
                #atualiza o menor caminho para o nó atual
                previous_nodes[neighbor] = current_min_node
 
        #removemos o nó da lista de nós não visitados
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

#Método responsável por printar o menor cainho, e seu peso
def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    #adiciona os nós na lista "path" em ordem inversa
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    #por fim, adiciona o nó inicial
    path.append(start_node)
    
    #print
    print('Menor camiho: ', end="")
    print(" -> ".join(reversed(path)))
    print(f'Peso do caminho: {shortest_path[target_node]}')

    minimun_path = (" ".join(reversed(path))).split(' ')
    weigth_min_path = shortest_path[target_node]
    return [minimun_path, weigth_min_path]

def show_min_path(start_node, target_node):
    #recebendo os nós e arestas da base de dados
    infos = read_data.get_nodes_and_edges()
    nodes, edges = infos[0], infos[1]

    #criando uma lista apenas com as labels dos nós, para ser adicionada no grafo
    formated_nodes = []
    for node in nodes:
        formated_nodes.append(node['label'])

    #criando um dicionário vazio com todos esses nós
    init_graph = {}
    for node in formated_nodes:
        init_graph[node] = {}

    #loop responsável por percorrer todas as arestas da base de dados
    for edge in edges:
        #na base de dados é informado os nós das arestas se baseando no "ID", e os nós foram adicionados de acordo com seu atribulo "label"
        #portanto, para adicionar a aresta corretamente precisamos achar o nó pelo id, e adicionar no dicionário pela label
        for node in nodes:
            #caso achou ao nó inicial
            if node['id'] == edge['source']:
                node_souce = node

            #caso achou o nó destinho
            elif node['id'] == edge['target']:
                node_target = node

        #adiciona a aresta, com seu peso, no dicionário
        init_graph[node_souce["label"]][node_target["label"]] = int(edge["weight"])

    #instancia um grafo com os nós e arestas da base de dados
    graph = Graph(formated_nodes, init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start_node)

    #resultado contendo [min_path, weight_min_path]
    result = print_result(previous_nodes, shortest_path, start_node=start_node, target_node=target_node)

    return result

show_min_path('32','45')