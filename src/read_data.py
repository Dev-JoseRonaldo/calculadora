#armazena a base de dados na variavel arq
arq = open("database/celegansneural.gml")

#armazena todas as linhas do arquivo na variável linhas
lines = arq.readlines()

#função responsável por tratar e retornar os dados no formato json
def get_nodes_and_edges():
    #json dos nós e arestas
    json_edges = []
    json_nodes = []

    #loop responsável por buscar todos os nós e arestas da base de dados e armazenar nas lista json
    for i in range(len(lines)):
        #tratando as linhas
        current_line = lines[i]
        current_line = " ".join(current_line.split())
        current_line = current_line.split(' ')

        #caso achou um nó na base de dados
        if current_line[0] == 'node':
            #id do nó está localizado 2 linhas abaixo da linha com o string "node"
            #em seguida tratamos a entrada para obter o id como inteiro
            line_id = lines[i + 2]
            line_id = " ".join(line_id.split())
            value_id = int(line_id.split(' ')[1])
            
            #label do nó está localizado 3 linhas abaixo da linha com o string "node"
            #em seguida tratamos a entrada para obter a label no formato desejado
            line_label = lines[i + 3]
            line_label = " ".join(line_label.split())
            value_label = line_label.split(' ')[1]
            value_label = value_label.replace('"', '')

            #adicona o nó na lista json de nós
            json_nodes.append({
                'id': value_id,
                'label': value_label,
            })

            #pula 3 linhas para não ler informações internas do nó adicionado
            i = i + 3

        #caso achou uma aresta na base de dados
        if current_line[0] == 'edge':
            #source da aresta está localizado 2 linhas abaixo da linha com o string "edge"
            #em seguida tratamos a entrada para obter o valor como esperado
            line_source = lines[i + 2]
            line_source = " ".join(line_source.split())
            value_source = int(line_source.split(' ')[1])

            #target da aresta está localizado 3 linhas abaixo da linha com o string "edge"
            #em seguida tratamos a entrada para obter o valor como esperado
            line_target = lines[i + 3]
            line_target = " ".join(line_target.split())
            value_target = int(line_target.split(' ')[1])

            #weight da aresta está localizado 4 linhas abaixo da linha com o string "edge"
            #em seguida tratamos a entrada para obter o valor como esperado
            line_weight = lines[i + 4]
            line_weight = " ".join(line_weight.split())
            value_weight = int(line_weight.split(' ')[1])

            #adicona a aresta na lista json de arestas
            json_edges.append({
                'source': value_source,
                'target': value_target,
                'weight': value_weight,
            })

            #pula 4 linhas para não ler informações internas do nó adicionado
            i = i + 4

    #retorna a lista com informações dos nós e arestas   
    return [json_nodes, json_edges]