from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection = 'mill',
            llcrnrlat = 25,
            llcrnrlon = -130,
            urcrnrlat = 90,
            urcrnrlon = 180,
            resolution = 'f')

m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color = 'b')

m.bluemarble()
xs = []
ys = []

NYClat, NYClon = 40.7127, -74.0059
xpt, ypt = m(NYClon, NYClat)
xs.append(xpt)
ys.append(ypt)

m.plot(xpt,ypt, 'co', markersize = 10)

LALlat, LALlon = 34.05, -118.0059
xpt, ypt = m(LALlon, LALlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt,ypt, 'g^', markersize = 10)

m.plot(xs, ys, color = 'r', linewidth=2, label='Flight 98')
#m.drawgreatcircle(NYClat, NYClon, LALlat, LALlon, label = 'Arc')
print(xs)
print(ys)
plt.legend()
plt.title("Mapp!")
plt.show()
