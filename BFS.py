# BFS algorithm in Python


import collections

# Cidades visitadas // deque mais facil para ser trabalhada em lista
def bfs(graph, starting_city, final_city):

    visited, fila = set(), collections.deque([starting_city])
    visited.add(starting_city)

    while fila:

        # Aqui ele retira um vertice da fila
        vertex = fila.popleft()
        print(str(vertex) + " ", end="")
        if final_city == str(vertex):
            exit()

        # Percorre todo o grafo pelo vértice e depois ele se atribui ao neighbour
        for neighbour in graph[vertex]:
            # O "visited" como dito, são as cidades visitadas
            # Caso ele nao for visitado ainda, ele vai voltar para a fila de cidades visitadas
            if neighbour not in visited:
                visited.add(neighbour)
            #Como diz a palavra "append", ela acrescenta uma cidade até a ultima. 
                fila.append(neighbour)

# Lista de cidades com ligações de acordo com o mapa
if __name__ == '__main__':
    graph = {
  'Oradea' : ['Zerind','Sibiu'],
  'Zerind' : ['Oradea', 'Arad'],
  'Arad' : ['Sibiu', 'Zerind', 'Timisoara'],
  'Sibiu' : ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
  'Rimnicu' : ['Sibiu', 'Pitesti', 'Craiova'],
  'Fagaras' : ['Sibiu', 'Bucharest'],
  'Pitesti' : ['Rimnicu', 'Craiova', 'Bucharest'],
  'Bucharest' : ['Urziceni', 'Giurgiu', 'Pitesti', 'Fagaras'],
  'Timisoara' : ['Arad', 'Lugoj'],
  'Lugoj' : ['Timisoara', 'Mehadia'],
  'Mehadia' : ['Lugoj', 'Dobreta'],
  'Dobreta' : ['Mehadia', 'Craiova',],
  'Craiova' : ['Dobreta', 'Pitesti', 'Rimnicu'],
  'Urziceni' : ['Bucharest', 'Vaslui', 'Hirsova'],
  'Giurgiu' : ['Bucharest'],
  'Vaslui' : ['Iasi'],
  'Iasi' : ['Neamt'],
  'Neamt' : ['Iasi'],
  'Hirsova' : ['Urziceni', 'Eforie'],
  'Eforie' : ['Hirsova']}

# Aqui ele solicita que o viajante/usuário defina sua origem e seu destino.
    starting_city = input("Escolha o seu ponto de partida \n")
    final_city = input("Escolha o seu ponto de parada: \n")
    print("\n****************************************")
    
    bfs(graph, starting_city, final_city)