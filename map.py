import folium
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

example = folium.Map(location=[35.85,128.6],zoom_start=12)

nodes =pd.read_csv('Daegu_node_1.csv')
links = pd.read_csv('Daegu_link_1.csv')

nodes = nodes[['NODE_ID','NODE_NAME','STNL_REG','Y','X']]
G_link = links[['F_NODE','T_NODE']]

layer1=folium.FeatureGroup(name='Reg')
layer2=folium.FeatureGroup(name='BC')
layer3=folium.FeatureGroup(name='CC')

for index, row in nodes.iterrows():
    location = (row['Y'], row['X'])
    folium.Circle(
        location=location,
        radius=70,
        color='red',
        fill_color='red'
    ).add_to(layer1)

Fpd = pd.DataFrame({'NODE_ID':list(links['F_NODE']), 'F_NODE': list(links['F_NODE'])})
Tpd = pd.DataFrame({'NODE_ID':list(links['T_NODE']), 'T_NODE': list(links['T_NODE'])})

Fno = pd.merge(nodes,Fpd,on='NODE_ID')
Tno = pd.merge(nodes,Tpd,on = 'NODE_ID')

Fpd = pd.DataFrame({'F_NODE':list(Fno['F_NODE']), 'F_Y': list(Fno['Y']), 'F_X' : list(Fno['X'])})
Tpd = pd.DataFrame({'T_NODE':list(Tno['T_NODE']), 'T_Y': list(Tno['Y']), 'T_X' : list(Tno['X'])})

new_link = pd.merge(G_link,Fpd, on = 'F_NODE')
new_link = pd.merge(new_link,Tpd, on = 'T_NODE')

#print(new_link)

for ix, row in new_link.iterrows():
    start = (row['F_Y'],row['F_X'])
    end = (row['T_Y'],row['T_X'])

    folium.PolyLine(
        locations=[start, end],
        color='blue',
        line_cap='round'
    ).add_to(layer1)

G = nx.Graph()

for idx,row in nodes.iterrows():
    G.add_node(row['NODE_ID'],Label=row['NODE_ID'],latitude=row['Y'], longitude=row['X'])

for idx, row in new_link.iterrows():
    G.add_edge(row['F_NODE'], row['T_NODE'])


nx.draw(G)
#plt.show()

BC = nx.betweenness_centrality(G)
CC =nx.closeness_centrality(G)

#print(CC)
#print(type(BC))

BC_keys = list(BC.keys())
BC_values = list(BC.values())

CC_keys = list(CC.keys())
CC_values = list(CC.values())

BC1 = pd.DataFrame({'NODE_ID':BC_keys, 'BC': BC_values})
CC1 = pd.DataFrame({'NODE_ID':CC_keys, 'CC': CC_values})

new_node = pd.merge(nodes,BC1, on = 'NODE_ID')
new_node = pd.merge(new_node,CC1, on = 'NODE_ID')

#print(new_node)

for index, row in new_node.iterrows():
    location = (row['Y'], row['X'])
    folium.Circle(
        location=location,
        radius=5000*row['BC'],
        color='yellow',
        fill_color='yellow'
    ).add_to(layer2)

for index, row in new_node.iterrows():
    location = (row['Y'], row['X'])
    folium.Circle(
        location=location,
        radius=9000*row['CC'],
        color='green',
        fill_color='green'
    ).add_to(layer3)

example.add_child(layer1)
example.add_child(layer2)
example.add_child(layer3)
example.add_child(folium.LayerControl())

example.save('example.html')