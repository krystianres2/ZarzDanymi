# C:\Users\kryst\OneDrive\Pulpit\Python\lab1\Scripts\activate
import folium
import pandas
m = folium.Map(location=(45.5236, -122.6750), tiles="cartodb positron")
data= pandas.read_csv("Volcanoes.txt")

for row in data.iterrows():
    folium.Marker(
        location=[row[1]["LAT"], row[1]["LON"]],
        popup=str(row[1]["ELEV"]) + " meters",
        icon=folium.Icon(color="green" if row[1]["ELEV"] < 1000 else "orange" if 1000 <= row[1]["ELEV"] < 3000 else "red"),
    ).add_to(m)

folium.Marker(
    location=[45.3288, -121.6625],
    tooltip="Click me!",
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(m)

folium.Marker(
    location=[45.3311, -121.7113],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="green"),
).add_to(m)


m.save("index.html")