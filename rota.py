alt = [3,4,7,4,6,4,34,4]
graph = {

'a' : {'b':3, 'c':4, 'd':7},
'b' : {'c':1, 'f':5},
'c' : {'f':6, 'd':2},
'd' : {'e':3, 'g':6},
'e' : {'g':3, 'h':4},
'f' : {'e':1, 'h':8},
'g' : {'h':2},
'h' : {'g':2}
}

def dijkstra(graph,start,goal):
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph
    infinity = 999999
    track_path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0


    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print("path is not reachable")
            break

    track_path.insert(0,start)

    if shortest_distance[goal] != infinity:
        print("shortest_distance is " + str(shortest_distance[goal]))
        print("optimal path is " + str(track_path))



dijkstra(graph,'a','h')
