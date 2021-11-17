#Roy Delgado
#roy.delgado63@myhunter.cuny.edu

import folium
import pandas as pd

df = pd.read_csv("Open_Restaurant_Applications.csv")
mapNYC = folium.Map(location=[40.75, -74.125], zoom_start=10, tiles="Stamen Watercolor")
restaurant = df.groupby(["NTA"]).get_group("Hudson Yards-Chelsea-Flatiron-Union Square")

for index,row in restaurant.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Restaurant Name"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapNYC)

mapNYC.save(outfile="Chelsea.html")
