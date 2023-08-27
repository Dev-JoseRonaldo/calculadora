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
  text1_canvas = canvas1.create_window( 420, 420, 
                                    anchor = "center",
                                    window = text_shortest_path)

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
    text_shortest_path['text'] = f'''Menor caminho: {string_shortest_path}
      Peso menor caminho: {weight_shortest_path}'''

    #botão que exibe o subgrafo 
    btn_show_subgraph = Button(text="exibir grafo menor caminho", width=26, command=lambda: show_shortest_path_graph(shortest_path))

    button3_canvas = canvas1.create_window(300, 450, 
                                       anchor = "nw",
                                       window = btn_show_subgraph)

  #caso informe alguma entrada inválida   
  except:
    text_shortest_path['text'] = 'Entradas inválidas'

#função responsável por exibir o subgrafo de menor caminho
def show_shortest_path_graph(path):
  path_id = []

  #convertendo lista de nós pela label, para lista de nós pelo id
  for node_path in path:
    for node in nodes:
      if node["label"] == node_path:
        path_id.append(node["id"])
        break
  
  #cria um grafo vazio
  subgraph = nx.DiGraph()

  #adicionando vertices
  for node in path:
    subgraph.add_node(node)

  #loop responsável por percorrer dtodos os nós do menor caminho
  for i in range(len(path_id)):
    #para o loop no ultimo nó
    if i == len(path_id) - 1:
      break
    
    #loop responsável por adicionar as arestas ao subgrafo
    for edge in edges:
      if edge['source'] == path_id[i] and edge['target'] == path_id[i + 1]:
        add_edge(subgraph, path[i], path[i + 1],edge['weight'])
        break

  #plotando o subgrafo
  plt.title("Grafo do menor caminho")
  pos = nx.spring_layout(subgraph)
  nx.draw_networkx(subgraph, pos=pos, node_color='red')
  labels = nx.get_edge_attributes(subgraph, 'weight')
  nx.draw_networkx_edge_labels(subgraph, pos=pos, edge_labels=labels)
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
window.geometry("800x550")
window.resizable(0, 0)

#criando a figura do grafo
plt.figure(1)

# Add image file
bg = PhotoImage(file = "image/bg.png")
  
# Create Canvas
canvas1 = Canvas( window, width = 800,
                 height = 550)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

#texto da interface
title_text = Label(window, text="")

#título da interface
title_text = Label(window, text="Dijkstra - Rede Neural", font=('Helvetica', 14))

#botão da interface que exibe o grafo principal
btn_view_main_graph = Button(window, text="Plotar Grafo Completo", command=plot_main_graph)

#input da interface: vértice inicial
v_source_field = Entry(width=5)
v_source_field.focus()

#input da interface: vértice destino
v_target_field = Entry(width=5)
v_target_field.focus()

#botão da interface: calcular menor caminho
btn_calc_shortest_path = Button(text="Calcular menor caminho", width=26, command=print_values)

#texto da interface: resultado menor caminho
text_shortest_path = Label(window, text="")

# #espacinho lado
# espacinho = Label(window, text="")
# espacinho.grid(column=0, row=0, rowspan=5, padx=75)

# #espacinho cima
# espacinho = Label(window, text="", width=0, height=0)
# espacinho.grid(column=2, row=0, columnspan=8, pady=50)

# Display Buttons
# title_text_canvas = canvas1.create_window( 250, 10, 
#                                        anchor = "nw",
#                                        window = title_text)

# Add Text
canvas1.create_text( 430, 30, text = "Dijkstra - Rede Neural", fill='white', font=('', 16))
canvas1.create_text( 420, 170, text = "Encontre a menor distancia entre dois vértices", fill='white', font=('', 14))
canvas1.create_text( 350, 231, text = "Vertice inicial:", fill='white', font=('', 14))
canvas1.create_text( 358, 271, text = "Vertice Destino:", fill='white', font=('', 14))

button1_canvas = canvas1.create_window( 340, 75, 
                                       anchor = "nw",
                                       window = btn_view_main_graph)

button2_canvas = canvas1.create_window( 300, 330, 
                                       anchor = "nw",
                                       window = btn_calc_shortest_path)

field1_canvas = canvas1.create_window( 422, 220, 
                                       anchor = "nw",
                                       window = v_source_field)

field2_canvas = canvas1.create_window( 440, 260, 
                                       anchor = "nw",
                                       window = v_target_field)



# button2_canvas = canvas1.create_window( 100, 40,
#                                        anchor = "nw",
#                                        window = button2)
  
# button3_canvas = canvas1.create_window( 100, 70, anchor = "nw",
#                                        window = button3)

#manter interface
window.mainloop()