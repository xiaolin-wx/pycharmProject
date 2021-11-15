import folium
import pandas as pd

latitude = 30.595350555555555555
longitude = 104.8895555

san_map = folium.Map(location=[latitude, longitude], zoom_start=21)

san_map.save('homeDataView01.html')