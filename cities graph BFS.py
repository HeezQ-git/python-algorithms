def BFS(start, end, num_nodes, graph):
    visited = [False] * num_nodes
    distance = [0] * num_nodes
    queue = []

    queue.append(start)
    visited[start] = True

    while queue:
        s = queue.pop(0)

        if s == end:
            print(distance[s])
            return

        if s not in graph: continue

        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[s] + 1
    print(-1)
    return

num_nodes = int(input())
graph = {}
graph_indexes = {}

counter = 0
for _ in range(num_nodes):
    edge = input().split(" ")

    for _edge in edge:
        if _edge not in graph_indexes:
            graph_indexes[_edge] = counter
            counter += 1

    if graph_indexes[edge[0]] not in graph: graph[graph_indexes[edge[0]]] = [graph_indexes[edge[1]]]
    else: graph[graph_indexes[edge[0]]].append(graph_indexes[edge[1]])
    
BFS(graph_indexes[input()], graph_indexes[input()], num_nodes, graph)
