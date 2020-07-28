import math
def haversine(lat1, lon1, lat2, lon2):

    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c
distances = []
      #a  b  c  d  e  f  g   h
lat = [22,22,44,55,44,21,14,23]
lon = [12,13,44,12,14,14,23,13]
for k in range(0,3):
    result = haversine(lat[k], lon[k],lat[k+1], lon[k+1])
    distances.append(result)

print(distances)
ba=haversine(lat[0], lon[0],lat[1], lon[1])
ca=haversine(lat[0], lon[0],lat[2], lon[2])
da=haversine(lat[0], lon[0],lat[3], lon[3])
cb=haversine(lat[1], lon[1],lat[2], lon[2])
fb=haversine(lat[1], lon[1],lat[4], lon[4])
fc=haversine(lat[2], lon[2],lat[4], lon[4])
dc=haversine(lat[2], lon[2],lat[3], lon[3])
ed=haversine(lat[3], lon[3],lat[5], lon[5])
gd=haversine(lat[3], lon[3],lat[6], lon[6])
ge=haversine(lat[5], lon[5],lat[6], lon[6])
he=haversine(lat[5], lon[5],lat[7], lon[7])
ef=haversine(lat[4], lon[4],lat[5], lon[5])
hf=haversine(lat[4], lon[4],lat[7], lon[7])
hg=haversine(lat[6], lon[6],lat[7], lon[7])
gh=haversine(lat[7], lon[7],lat[6], lon[6])
graph = {

'a' : {'b':ba, 'c':ca, 'd':da},
'b' : {'c':cb, 'f':fb},
'c' : {'f':fc, 'd':dc},
'd' : {'e':ed, 'g':gd},
'e' : {'g':ge, 'h':he},
'f' : {'e':ef, 'h':hf},
'g' : {'h':hg},
'h' : {'g':gh}
}

alt = [33,34,32,37,29,40,34,35]
graph2 = {

'a' : {'b':alt[1]-alt[0], 'c':alt[2]-alt[0], 'd':alt[3]-alt[0]},
'b' : {'c':alt[2]-alt[1], 'f':alt[4]-alt[1]},
'c' : {'f':alt[4]-alt[2], 'd':alt[3]-alt[2]},
'd' : {'e':alt[5]-alt[3], 'g':alt[6]-alt[3]},
'e' : {'g':alt[6]-alt[5], 'h':alt[7]-alt[5]},
'f' : {'e':alt[5]-alt[4], 'h':alt[7]-alt[4]},
'g' : {'h':alt[7]-alt[6]},
'h' : {'g':alt[6]-alt[7]}
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
