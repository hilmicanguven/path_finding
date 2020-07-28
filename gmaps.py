import folium
m = folium.Map(location = [39.766705, 30.525631], tiles = "OpenStreetMap", zoom_start = 45)


folium.Marker(location=[47.606209, -122.332069],popup='Seattle',icon=folium.Icon(icon='cloud')).add_to(m)
folium.Marker(location=[37.774929, -122.419418],popup='San Fransisco',icon=folium.Icon(color='green')).add_to(m)
folium.Marker(location=[41.878113, -87.629799],popup='Chicago',icon=folium.Icon(color='red', icon='envelope')).add_to(m)

m.save('index.html')
