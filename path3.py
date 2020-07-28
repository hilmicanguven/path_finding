from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import folium


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


      #a  b  c  d  e  f  g   h
lat = [39.7902699, 39.7893960, 39.7897752, 39.7904247, 39.7882418, 39.7876153, 39.7911107, 39.7902369]
lon = [30.4830909, 30.4917812, 30.4942060, 30.4982183, 30.5007720, 30.4958797, 30.5028534, 30.5054712]
alti =[50, 48, 40, 60, 50, 51, 48.2, 49 ]


ba=haversine(lat[0], lon[0],lat[1], lon[1])*abs(alti[0]-alti[1])
ca=haversine(lat[0], lon[0],lat[2], lon[2])*abs(alti[0]-alti[2])
da=haversine(lat[0], lon[0],lat[3], lon[3])*abs(alti[0]-alti[3])
cb=haversine(lat[1], lon[1],lat[2], lon[2])*abs(alti[2]-alti[1])
fb=haversine(lat[1], lon[1],lat[4], lon[4])*abs(alti[4]-alti[1])
fc=haversine(lat[2], lon[2],lat[4], lon[4])*abs(alti[4]-alti[2])
dc=haversine(lat[2], lon[2],lat[3], lon[3])*abs(alti[1]-alti[3])
ed=haversine(lat[3], lon[3],lat[5], lon[5])*abs(alti[3]-alti[5])
gd=haversine(lat[3], lon[3],lat[6], lon[6])*abs(alti[3]-alti[6])
ge=haversine(lat[5], lon[5],lat[6], lon[6])*abs(alti[5]-alti[6])
he=haversine(lat[5], lon[5],lat[7], lon[7])*abs(alti[5]-alti[7])
ef=haversine(lat[4], lon[4],lat[5], lon[5])*abs(alti[4]-alti[5])
hf=haversine(lat[4], lon[4],lat[7], lon[7])*abs(alti[4]-alti[7])
hg=haversine(lat[6], lon[6],lat[7], lon[7])*abs(alti[6]-alti[7])
gh=haversine(lat[7], lon[7],lat[6], lon[6])*abs(alti[7]-alti[6])
print("ba " + str(ba))
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


    return track_path


track_path =dijkstra(graph,'a','h')


m = folium.Map(location = [lat[0], lon[0]], tiles = "OpenStreetMap", zoom_start = 45)
lines = []
for points in track_path:
    if points == 'a':
        folium.Marker(location=[lat[0], lon[0]],popup='Baslangıc Noktası').add_to(m)
        lines.append([lat[0], lon[0]])
    elif points == 'b':
        folium.Marker(location=[lat[1], lon[1]],popup='Eskisehir', tooltip = "click for more").add_to(m)
        lines.append([lat[1], lon[1]])
    elif points == 'c':
        folium.Marker(location=[lat[2], lon[2]],popup='Eskisehir', tooltip = "click for more").add_to(m)
        lines.append([lat[2], lon[2]])
    elif points == 'd':
        lines.append([lat[3], lon[3]])
        folium.Marker(location=[lat[3], lon[3]],popup='d',icon=folium.Icon(color='green')).add_to(m)
    elif points == 'e':
        lines.append([lat[4], lon[4]])
        folium.Marker(location=[lat[4], lon[4]],popup='e',icon=folium.Icon(color='green')).add_to(m)
    elif points == 'f':
        lines.append([lat[5], lon[5]])
        folium.Marker(location=[lat[5], lon[5]],popup='f',icon=folium.Icon(color='green')).add_to(m)
    elif points == 'g':
        folium.Marker(location=[lat[6], lon[6]],popup='g',icon=folium.Icon(color='green')).add_to(m)
        lines.append([lat[6], lon[6]])
    elif points == 'h':
        lines.append([lat[7], lon[7]])
        folium.Marker(location=[lat[7], lon[7]],popup='h',icon=folium.Icon(color='green')).add_to(m)

folium.PolyLine(lines, color="red", weight=4.5, opacity=1).add_to(m)
m.save('index.html')

"""
m = Basemap(projection = 'cyl',
            llcrnrlat = 36,
            llcrnrlon = 26,
            urcrnrlat = 42,
            urcrnrlon = 45,
            resolution = 'f')

m.drawcoastlines()
m.drawcountries(linewidth=2)
#m.drawstates(color = 'b')

m.bluemarble()

xs = []
ys = []
print(track_path)
#track_path=['a', 'd', 'g', 'h']
for point in track_path:
    if point == 'a':
        print(point)
        a1, a2 = lon[0], lat[0]
        print(a1)
        axpt, aypt = m(a1, a2)
        print(axpt)
        xs.append(axpt)
        ys.append(aypt)
        m.plot(axpt,axpt, 'co', markersize = 1)
    elif point == 'b':
        print(point)
        b1, b2 = lon[1], lat[1]
        bxpt, bypt = m(b1, b2)
        xs.append(bxpt)
        ys.append(bypt)
        m.plot(bxpt,bypt, 'co', markersize = 1)
    elif point == 'c':
        print(point)
        c1, c2 = lon[2], lat[2]
        xpt, ypt = m(c1, c2)
        xs.append(cxpt)
        ys.append(cypt)
        m.plot(cxpt,cypt, 'co', markersize = 1)
    elif point == 'd':
        print(point)
        d1, d2 = lon[3], lat[3]
        dxpt, dypt = m(d1, d2)
        xs.append(dxpt)
        ys.append(dypt)
        m.plot(dxpt,dypt, 'co', markersize = 1)
    elif point == 'e':
        print(point)
        e1, e2 = lon[5], lat[5]
        expt, eypt = m(e1, e2)
        xs.append(expt)
        ys.append(eypt)
        m.plot(expt,eypt, 'co', markersize = 1)
    elif point == 'f':
        print(point)
        f1, f2 = lon[4], lat[4]
        fxpt, fypt = m(f1, f2)
        xs.append(fxpt)
        ys.append(fypt)
        m.plot(fxpt,fypt, 'co', markersize = 1)
    elif point == 'g':
        print(point)
        g1, g2 = lon[6], lat[6]
        gxpt, gypt = m(g1, g2)
        xs.append(gxpt)
        ys.append(gypt)
        m.plot(gxpt,gypt, 'co', markersize = 1)
    elif point == 'h':
        print(point)
        h1, h2 = lon[7], lat[7]
        hxpt, hypt = m(h1, h2)
        xs.append(hxpt)
        ys.append(hypt)
        m.plot(hxpt,hypt, 'co', markersize = 1)

print(xs)
print(ys)

m.plot(xs, ys, color = 'r', linewidth=2, label='Flight 98')
#m.drawgreatcircle(NYClat, NYClon, LALlat, LALlon, label = 'Arc')

plt.legend()
plt.title("Mapp!")
plt.show()
"""
