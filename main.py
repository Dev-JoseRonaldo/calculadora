import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
import src.read_data as read_data
import src.dijkstra as dijkstra

#função responsável por adicionar uma aresta com peso no grafo
def add_edge(G, u, v, w=1):
  G.add_edge(u, v, weight=w)

#função responsável por plotar o grao principal com todos os nós e aretas inseridos
def plot_main_graph():
  plt.title("Grafo completo")
  nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
  plt.show()

#função responsável por exibir os outputs da consulta em tela, de acordo com os inputs fornecidos
def print_values():
  text_shortest_path['text'] = ''

  v_source = v_source_field.get()
  v_target = v_target_field.get()

  #caso há campos vazios, imprime mensagem de erro
  if v_source == '' or v_target == '':
    text_shortest_path['text'] = 'Por favor preencha todos os campos'
    return
  
  #caso os vértices de inicio e destino são iguais, imprime mensagem de erro
  if v_source == v_target:
    text_shortest_path['text'] = 'Insira vértice inicial e vértice de destino diferentes'
    return
  
  #tenta mostrar menor caminho entre dois vértices
  try:
    #como no grafo os nós estão salvos pela label, precisamos encontrar os nós pela label, uma vez que, o id da base de dados não tem relação com os nós do caminho, e sim com o id da label do nó digitado no input
    #em seguida, tratamos os dados para o output
    result = dijkstra.show_min_path(v_source,v_target)
    shortest_path, weight_shortest_path = result[0], result[1]
    string_shortest_path = " -> ".join(shortest_path)

    #texto do menor caminho
    text_shortest_path['text'] = f'''
      Menor caminho: {string_shortest_path}
      Peso menor caminho: {weight_shortest_path}'''

    #botão que exibe o subgrafo 
    btn_show_subgraph = Button(text="exibir grafo menor caminho", width=26, command=lambda: show_shortest_path_graph(shortest_path))
    btn_show_subgraph.grid(row=8, column=1, columnspan=2)

  #caso informe alguma entrada inválida   
  except:
    text_shortest_path['text'] = 'Entradas inválidas'

#função responsável por exibir o subgrafo de menor caminho
def show_shortest_path_graph(path):
  plt.title("Grafo do menor caminho")
  pos = nx.spring_layout(G)
  subgraph = G.subgraph(path)
  nx.draw_networkx(subgraph, pos=pos, node_color = 'red')
  plt.show()

#recebendo as informações dos nós e arestas da base de dados
infos = read_data.get_nodes_and_edges()
nodes, edges = infos[0], infos[1]

#formatando as arestas no formato exigido pelo networkx
formated_edges = []
for edge in edges:
  formated_edges.append((str(edge['source']),str(edge['target']),edge['weight']))

#cria um grafo vazio
G = nx.Graph()

#adicionando vertices
for node in nodes:
  G.add_node(node['label'])

#adicionando arestas
for edge in edges:
  #na base de dados é informado os nós das arestas se baseando no "ID", e os nós foram adicionados no grafo de acordo com seu atribulo "label"
  #portanto, precisamos achar o nó pela label e verificar seu id para adicionar a aresta corretamente
  for node in nodes:
    #encontrando o nó incial da aresta
    if node['id'] == edge['source']:
      source_node = node

    #encontrando o nó final da aresta
    elif node['id'] == edge['target']:
      target_node = node

  #adiciona a aresta ao grafo caso encontre os dois nós 
  if source_node and target_node:
    add_edge(G, str(source_node['label']),str(target_node['label']),edge['weight'])


#criando a interface
window = Tk()
window.title("algoritmos e estrutura de dados")
window.geometry("800x800")
window.config(padx=175, pady=10)
window.resizable(0, 0)

#criando a figura do grafo
plt.figure(1)

#título da interface
title_text = Label(window, text="Trabalho algoritmos e estrutura de dados")
title_text.grid(column=1, row=0, padx=10, pady=10)

#botão da interface que exibe o grafo principal
btn_view_main_graph = Button(window, text="Plotar Grafo Completo", command=plot_main_graph)
btn_view_main_graph.grid(column=1, row=1, padx=10, pady=10)

#texto da interface
title_text = Label(window, text="Encontre a menor distancia entre dois vértices")
title_text.grid(column=1, row=3, padx=10, pady=20)

#input da interface: vértice inicial
v_source_label = Label(text="Vertice inicial:")
v_source_label.grid(row=4, column=0, pady=1)
v_source_field = Entry(width=30)
v_source_field.grid(row=4, column=1, pady=1)
v_source_field.focus()

#input da interface: vértice destino
v_target_label = Label(text="Vertice destino:")
v_target_label.grid(row=5, column=0, pady=1)
v_target_field = Entry(width=30)
v_target_field.grid(row=5, column=1, pady=1)
v_target_field.focus()

#botão da interface: vértice destino
btn_calc_shortest_path = Button(text="Calcular menor caminho", width=26, command=print_values)
btn_calc_shortest_path.grid(row=6, column=1, pady=5)

#texto da interface: vértice destino
text_shortest_path = Label(window, text="")
text_shortest_path.grid(column=1, row=7, padx=10, pady=10)

#manter interface
window.mainloop()