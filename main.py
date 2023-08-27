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
  nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True, node_size=500)
  plt.show()

#função responsável por exibir os outputs da consulta em tela, de acordo com os inputs fornecidos
def print_values():
  text_shortest_path['text'] = ''
  text1_canvas = canvas.create_window(510, 450, anchor = "center", window = text_shortest_path)

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
    btn_show_subgraph = Button(window,
                            text="exibir grafo menor caminho", 
                            command=lambda: show_shortest_path_graph(shortest_path),
                            font=('Times New Roman CE', 12, 'bold'), 
                            bg="white", 
                            foreground="black", 
                            activebackground="#001F48", 
                            activeforeground="white")

    btn_show_subgraph_canvas = canvas.create_window(375, 480, anchor = "nw", window = btn_show_subgraph)

  #caso informe alguma entrada inválida   
  except:
    text_shortest_path['text'] = f'Nenhum caminho encontrado entre "{v_source}" e "{v_target}"'

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
  nx.draw_networkx(subgraph, pos=pos, node_color='red', node_size=800, font_color="white", font_weight="bold")
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
window.title("Projeto de algoritmos e estrutura de dados")
window.geometry("1000x687")
window.resizable(0, 0)

#criando a figura do grafo
plt.figure(1)

# Add image file
bg = PhotoImage(file = "image/bg.png")
  
# Create Canvas
canvas = Canvas(window, width = 1000, height = 687)
canvas.pack(fill = "both", expand = True)
  
# Display image
canvas.create_image( 0, 0, image = bg, anchor = "nw")

#botão da interface que exibe o grafo principal
btn_view_main_graph = Button(window, 
                             text="Plotar Grafo Completo", 
                             command=plot_main_graph, 
                             font=('Times New Roman CE', 12, 'bold'), 
                             bg="white", 
                             foreground="black", 
                             activebackground="#001F48", 
                             activeforeground="white")

#input da interface: vértice inicial
v_source_field = Entry(width=5)
v_source_field.focus()

#input da interface: vértice destino
v_target_field = Entry(width=5)

#botão da interface: calcular menor caminho
btn_calc_shortest_path = Button(window,
                                text="Calcular menor caminho", 
                                command=print_values, 
                                font=('Times New Roman CE', 12, 'bold'), 
                                bg="white", 
                                foreground="black", 
                                activebackground="#001F48", 
                                activeforeground="white")

#texto da interface: resultado menor caminho
text_shortest_path = Label(window, text="")

#renderizando elementos no canvas
canvas.create_text( 530, 80, text = "Rede Neural do Caenorhabditis Elegans", fill='white', font=('Times New Roman CE', 22, 'bold'))
canvas.create_text( 520, 150, text = "Visualize o grafo completo:", fill='white', font=('', 14))
canvas.create_text( 520, 260, text = "Encontre o menor caminho entre dois neurônios na rede neural:", fill='white', font=('Times New Roman CE', 16))
canvas.create_text( 480, 301, text = "Neurônio Inicial:", fill='white', font=('Times New Roman CE', 14))
canvas.create_text( 475, 331, text = "Neurônio Final:", fill='white', font=('Times New Roman CE', 14))
btn_view_main_graph_canva = canvas.create_window(400, 175, anchor = "nw", window = btn_view_main_graph)
btn_calc_shortest_path_canva = canvas.create_window(390, 380, anchor = "nw", window = btn_calc_shortest_path)
v_source_field_canva = canvas.create_window(570, 290, anchor = "nw", window = v_source_field)
v_target_field_canva = canvas.create_window(570, 320, anchor = "nw", window = v_target_field)

#manter interface
window.mainloop()