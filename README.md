# <p align="center"> Projeto Dijkstra - Algorimos e estrutura de dados </p>

<p align="center">
  <img alt="ignite feed" src="https://res.cloudinary.com/devjoseronaldo/image/upload/v1693180158/projeto-algoritmo/banner.png" width="100%">
</p>

<br/>

## 📝 Contexto do problema

A nossa base de dados é uma rede direcionada e ponderada que representa a rede neural do Caenorhabditis elegans ou C. Elegans, um verme nematódeo que foi de extrema importância no estudo de exploração das doenças humanas. Os dados com informações da rede neural do C. Elegans foram retirados do site do Prof. Duncan Watts na Universidade de Columbia, http://cdg.columbia.edu/cdg/datasets e foram compilados por Duncan Watts e Steven Strogatz dos dados experimentais originais por White et al. e disponibilizados na Internet. Dados experimentais originais obtidos de J. G. White, E. Southgate, J. N. Thompson, e S. Brenner, Phil. Trans. R. Soc. London 314, 1-340 (1986).

Base de dados: Rede neural de C. Elegans - http://www-personal.umich.edu/~mejn/netdata/

A base contém informações de um grafo e é composta por nós e arestas com atributos associados. Os nós são rotulados com IDs e valores(labels), e as arestas fazem a conexão entre esses nós com valores específicos.
Os nós são no formato: Nó 1: ID 1, Rótulo "51"
As arestas são no formato: Aresta do Nó 137 para o Nó 89 com um valor de 3.

<br/>

## 👨🏿‍💻 Implementação

### Algoritmo utilizado: ``` Dijkstra ```

### Desenvolvimento: 
- Escolhemos uma base de dados que atendesse aos requisitos do projeto.
- Criamos o projeto no github para ir atualizando a cada nova funcionalidade implementada.
- Criamos um código para que pudéssemos acessar os dados do arquivo e tratamos esses dados linha a linha para podermos utilizá-los no nosso programa de acordo com a forma que algumas bibliotecas exigiam.
- Ao final desse processo, armazenamos todos os nós e arestas em uma lista no formato json que contém as informações associadas a cada um.
- Criamos a classe Graph com alguns métodos para criar o nosso gráfico. 
- Implementamos o algoritmo de menor caminho do algoritmo Dijkstra
- Além do algoritmo dijkstra, criamos alguns outros métodos na criação do grafo, foram eles:
  - método para armazenar as conexões entre os nós adjacentes
  - método para saber o peso de uma aresta entre dois nós
  - método para retornar os nós do grafo
  - método para imprimir o resultado da consulta na tela do usuário
  - método para adicionar uma aresta com peso
  - método para plotar o gráfico principal
  - método de mostrar o menor caminho entre os pontos escolhidos pelo usuário.

- Na base de dados, os nós possuem duas informações: id e label. Os nós são adicionados no grafo pelo seu atributo “label”. No entanto, na inserção de arestas, nosso código precisa se basear no atributo “ID”, uma vez que as arestas presentes na base de dados faz referência ao ID do nó. Portanto, para adicionar uma aresta, é preciso achar o nó pelo label e verificar seu ID.
- Pensamos em como seria a interface gráfica do nosso programa e como seria a visualização dos dados
- Na parte de interface do nosso programa nós criamos algumas funções:
  - função de adicionar uma aresta com peso no grafo
  - função para plotar o grafo principal com todos os nós e arestas inseridos
  - função que exibe outputs de acordo com as entradas do usuário (caso o usuário tente calcular o caminho de origem e destino com o mesmo nó, caso o usuário tente calcular o menor caminho enquanto um campo ainda está vazio ou coloque nós que não existem no grafo)
  - função que exibe o subgrafo apenas com os nós que fazem parte do menor caminho encontrado pelo algoritmo com a exibição de um subgrafo direcionado do grafo principal.

- No grafo, os nós estão sendo salvos pelos números informados na label. Dessa forma, para encontrar o menor caminho entre os dois nós, é preciso encontrar os nós pela label, uma vez que o id das arestas salvas na base de dados não tem relação com as labels dos nós do caminho impressos no grafo, e sim com o id do nó que contém o label digitado no input.
- Tratamos os dados do menor caminho que são impressos na tela do usuário

- Na nossa interface temos 3 botões: 
  - Botão de visualização do grafo completo com todos os nós e arestas
  - Botão que calcula o menor caminho entre dois nós
  - Botão de visualização de menor caminho, que exibe um subgrafo com o menor caminho entre os nós inseridos pelo usuário

- Adicionamos uma imagem de background que tem relação com a base de dados escolhida no nosso projeto na interface e inserimos alguns títulos para que ficasse o mais intuitivo possível para o usuário final.

- também validamos as entradas fornecidas pelo usuário nos inputs, dessa forma, ao receber um input inválido, nosso programa exibe diferentes mensagens de erro dependendo da entrada digitada.

<br/>

### 📚 Bibliotecas utilizadas:
- [Matplotlib](https://matplotlib.org/): Utilizamos a biblioteca Matplotlib para exibir o grafo principal e o subgrafo.
- [Networkx](https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx.html): Utilizamos a biblioteca Networkx para criar o grafo principal e o subgrafo direcionado. Utilizamos algumas de suas ferramentas para melhorar a visualização dos grafos e deixar elas mais simples e intuitivas para os usuários.
- [Tkinter](https://docs.python.org/3/library/tkinter.html):Utilizamos a biblioteca Tkinter para a criação da nossa interface gráfica de usuário, com ela criamos a janela de consulta de dados, os botões exibidos na janela, adicionamos uma imagem no background da janela e também a algumas caixas de texto impressas na janela.
- [Sys](https://docs.python.org/3/library/sys.html):Utilizamos a biblioteca sys para acessar a constante maxsize que representa o maior valor inteiro suportado pela arquitetura do sistema, como se fosse um número infinito dentro do código. Utilizamos esse valor de constante grande para iniciar o valor de menor caminho antes de fazer os cálculos de menor caminho entre os nós.

<br/>

## 💻 Projeto

###  Para visualizar o funcionamento do projeto, acesse o vídeo abaixo:
[Clique aqui para ser redirecionado ao vídeo](https://www.youtube.com/watch?v=lCcR7y_wR_w)

###  Para rodar o projeto localmente em seu computador, siga as instruções abaixo:
```bash
# Clone o projeto
# Abra o seu terminal e execute o comando abaixo
$ git clone https://github.com/Dev-JoseRonaldo/Dijkstra.git

# Rode o projeto
$ execute o arquivo main.py em seu editor favorito

# Instale todas as bibliotecas necessárias
$ Verifique a mensagem de erro em seu terminal para identificar todas as bibliotecas necessárias

# Rode o projeto
$ execute novamente o arquivo main.py

```

### Imagens:

- Tela inicial do sistema
  
<p align="center">
  <img alt="Tela inicial do sistema" src="https://res.cloudinary.com/devjoseronaldo/image/upload/v1693180158/projeto-algoritmo/banner.png" width="100%">
</p>

- Cálculo e exibição do menor caminho
  
<p align="center">
  <img alt="Cálculo e exibição do menor caminho" src="https://res.cloudinary.com/devjoseronaldo/image/upload/v1693180158/projeto-algoritmo/print_system.png" width="100%">
</p>


- Exibição do grafo do menor caminho
  
<p align="center">
  <img alt="Exibição do grafo do menor caminho" src="https://res.cloudinary.com/devjoseronaldo/image/upload/v1693180157/projeto-algoritmo/plot_graph_min_path.png" width="100%">
</p>

- Exibição do grafo completo
  
<p align="center">
  <img alt="Exibição do grafo completo" src="https://res.cloudinary.com/devjoseronaldo/image/upload/v1693180158/projeto-algoritmo/plot_main_graph.png" width="100%">
</p>

<br/>

## 📌 Conclusão:
 O programa lê o arquivo da base de dados que escolhemos, trata os dados e cria um grafo com as informações presentes no arquivo. É possível ter uma visualização do grafo completo clicando no botão “Plotar Grafo Completo”. Ao clicar no botão “Calcular menor caminho”, o  algoritmo Dijkstra de menor caminho calcula a menor distância entre os dois pontos do grafo que foram escolhidos pelo usuário. O programa exibe na tela uma caixa de texto com as informações dos nós que fazem parte do menor caminho.  Se existir um caminho entre os dois nós inseridos pelo usuário, após o cálculo ser feito, abaixo da caixa de texto um novo botão será exibido. Ao clicar no novo botão “ exibir grafo de menor caminho”, um subgrafo direcionado apenas com os nós que fazem parte do menor caminho será exibido na tela. Caso o usuário se depare com um dos seguintes erros: tentar calcular o caminho de origem e destino com o mesmo nó, tentar calcular o menor caminho enquanto um campo de entrada  ainda está vazio, tentar fazer o cálculo com nós que não existem no grafo,  uma mensagem será impressa na tela.

<br/>

## 🔎 Referências

### Base de dados:
Alex arenas datasets. Disponível em: <https://deim.urv.cat/~alexandre.arenas/data/welcome.htm>. Acesso em: 20  ago.  2023.
Disponível em: <http://cdg.columbia.edu/cdg/datasets>. Acesso em: 20  ago.  2023.

### Algoritmo Dijkstra:

KLOCHAY, A. Implementing Dijkstra’s algorithm in Python. Disponível em: <https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html>. Acesso em: 22  ago.  2023.

aula1-Conceitos-fundamentais. Disponível em: <https://edisciplinas.usp.br/pluginfile.php/7544320/mod_resource/content/1/aula1-Conceitos-fundamentais.html>. Acesso em: 22 ago. 2023.

<br/>

## Autores

| [<img src="https://github.com/vitoriabtriz.png" width=115><br><sub>Vitória Beatriz</sub><br>](https://github.com/vitoriabtriz) <sub>Desenvolvedora</sub><br> <sub>[Linkedin](https://www.linkedin.com/in/vitoriabtriz)</sub><br> <sub> Portfolio </sub> | [<img src="https://github.com/dev-joseronaldo.png" width=115><br><sub>José Ronaldo</sub><br>](https://github.com/Dev-JoseRonaldo) <sub>Desenvolvedor</sub><br> <sub>[Linkedin](https://www.linkedin.com/in/devjoseronaldo/)</sub><br> <sub>[Portfólio](https://joseronaldo.netlify.app/)</sub> |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
