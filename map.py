import folium
import pandas
import json

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
el=list(data["ELEV"])

def colour_producer(elev):
    if elev<2000:
        return "green"
    elif elev<3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location =[38,-99],zoom_start=6)
fgv=folium.FeatureGroup(name="Volcanoes")

for lt,ln,e in zip(lat,lon,el):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=7,popup=folium.Popup(str(e)+" m",parse_html=True,max_width=70),fill_color=colour_producer(e),color='grey',fill=True,fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000<= x['properties']['POP2005']< 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")