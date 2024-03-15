# C:\Users\kryst\OneDrive\Pulpit\Python\lab1\Scripts\activate
import folium
import pandas
import json
m = folium.Map(location=(45.5236, -122.6750), tiles="cartodb positron")
data= pandas.read_csv("Volcanoes.txt")
cordinates = json.load(open("world.json"))

html = '''
Nazwa wulkanu: 
<p style="color:purple; text-decoration:underline; margin=0; !important;">{}</p> 
Wysokość: {} m

'''

for row in data.iterrows():
    folium.CircleMarker(
        location=[row[1]["LAT"], row[1]["LON"]],
        popup=folium.Popup(html.format(row[1]["NAME"], row[1]["ELEV"]), max_width=200),
        color="grey",
        fill=True,
        fill_color="green" if row[1]["ELEV"] < 1000 else "orange" if 1000 <= row[1]["ELEV"] < 3000 else "red",
        fill_opacity=0.8,
    ).add_to(m)

def style_function(feature):
    # Get the population of the feature
    population = feature['properties']['POP2005']

    # Determine fill color based on population
    if population < 1000000:
        fill_color = 'green'
    elif population < 10000000:
        fill_color = 'yellow'
    elif population == 0:
        fill_color = 'grey'
    else:
        fill_color = 'red'

    return {
        'fillColor': fill_color,
        'color': 'blue',
        'weight': 2,
    }
folium.GeoJson(cordinates,style_function=style_function).add_to(m)

for feature in cordinates['features']:
    print((feature['properties']['POP2005'])/1000000)

# # Extract exterior coordinates of each polygon
# exterior_coordinates = [feature['geometry']['coordinates'][0] for feature in cordinates['features']]

# # Add polygons to the map
# for coords in exterior_coordinates:
#     folium.Polygon(
#         locations=coords,
#         color="red",
#         weight=6,
#     ).add_to(m)

# folium.Polygon(
#     locations= cordinates,
#     color="grey",
# ).add_to(m)

# folium.Marker(
#     location=[45.3288, -121.6625],
#     tooltip="Click me!",
#     popup="Mt. Hood Meadows",
#     icon=folium.Icon(icon="cloud"),
# ).add_to(m)

# folium.Marker(
#     location=[45.3311, -121.7113],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="green"),
# ).add_to(m)


m.save("index.html")