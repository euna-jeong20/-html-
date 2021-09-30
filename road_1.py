import folium
import pandas as pd

nodes =pd.read_csv('Daegu_node_1.csv')

nodes = nodes[['NODE_ID','Y','X','STNL_REG']]
#점,위도,경도

print(type(nodes))

print(nodes)
print(nodes)
example = folium.Map(location=[35.85,128.6],zoom_start=12)

folium.CircleMarker(
    location=[35.8888403,128.608111],
    popup='KNU',
    icon=folium.Icon(color = 'red',icon = 'star')
).add_to(example)

folium.PolyLine([(35.8888403,128.608111),(35.88,128.6)])
example.save('example.html')
