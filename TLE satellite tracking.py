
from beyond import config
from beyond.io.tle import Tle
from beyond.orbits import orbit
from beyond.dates import Date, timedelta
from matplotlib.markers import MarkerStyle
import matplotlib.pyplot as plt
import numpy as np

# ---------- Processing the TLE ------------ #

tle = Tle("""ESTCUBE 1             
1 39161U 13021C   21194.17037475  .00000181  00000-0  36265-4 0  9994
2 39161  97.9384 274.7701 0010757  70.9635 289.2771 14.72499082439536""")

orb_est = tle.orbit() # orbit for EstCube
period = orb_est.infos.period
start = Date.now()
stop = 2 * period
z = 200
step = period/z

# Tables containing the positions of the ground track
latitudes, longitudes = [], []
prev_lon, prev_lat = None, None


for point in orb_est.ephemeris(start=start, stop=stop, step=step):

    # Conversion to earth rotating frame
    point.frame = 'ITRF'

    # Conversion from cartesian to spherical coordinates (range, latitude, longitude)
    point.form = 'spherical'

    # Conversion from radians to degrees
    lon, lat = np.degrees(point[1:3])
    
    # Creation of multiple segments in order to not have a ground track
    # doing impossible paths
    
    if prev_lon is None:
        lons = []
        lats = []
        longitudes.append(lons)
        latitudes.append(lats)
    elif orb_est.i < np.pi /2 and (np.sign(prev_lon) == 1 and np.sign(lon) == -1):
        lons.append(lon + 360)
        lats.append(lat)
        lons = [prev_lon - 360]
        lats = [prev_lat]
        longitudes.append(lons)
        latitudes.append(lats)
    elif orb_est.i > np.pi/2 and (np.sign(prev_lon) == -1 and np.sign(lon) == 1):
        lons.append(lon - 360)
        lats.append(lat)
        lons = [prev_lon + 360]
        lats = [prev_lat]
        longitudes.append(lons)
        latitudes.append(lats)

    lons.append(lon)
    lats.append(lat)
    prev_lon = lon
    prev_lat = lat

# ----------- Plotting ----------------#
from itertools import chain
longitudes = list(chain.from_iterable(longitudes))
longitudes = [round(num) for num in longitudes]
latitudes = list(chain.from_iterable(latitudes))
latitudes = [round(num) for num in latitudes]
coordinates = list(zip(latitudes,longitudes))

import folium
m = folium.Map(location=[0,0], zoom_start=1.5)
folium.CircleMarker(coordinates[0],color='red',radius=5).add_to(m) # end point
folium.CircleMarker(coordinates[len(coordinates)-1],color='green',radius=5).add_to(m) # starting point

for i in range(len(coordinates)):
    folium.Circle(coordinates[i]).add_to(m)


# --------- Grid ------------- # 
lat_interval = 10
lon_interval = 10
lat_trans = 1
long_trans = 5
grid = []
grid_trans = []

for lat in range(-90, 90, lat_interval):
    grid.append([[lat, -180],[lat, 180]])

for lon in range(-180, 181, lon_interval):
    grid.append([[-90, lon],[90, lon]])

for g in grid:
    folium.PolyLine(g, color="black",weight=0.5, opacity=0.5).add_to(m)

folium.PolyLine([[0,-180],[0,180]],tooltip="Equator", color="green", weight=2).add_to(m) # equator
folium.PolyLine([[-90,-0],[90,0]], color="green", weight=1.8).add_to(m) # prime meridian
m.save('Test3.html')