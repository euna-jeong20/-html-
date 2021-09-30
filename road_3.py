import networkx as nx
import pandas as pd

G = nx.gnp_random_graph(10,0.2)

BC = nx.betweenness_centrality(G)
CC =nx.closeness_centrality(G)
'''print(BC)
print(type(BC))

print(BC.keys())
print(BC.values())
#print(type(BC.keys()))'''

BC_keys = list(BC.keys())
BC_values = list(BC.values())

CC_keys = list(CC.keys())
CC_values = list(CC.values())

BC1 = pd.DataFrame({'node':BC_keys, 'BC': BC_values})
CC1 = pd.DataFrame({'node':CC_keys, 'CC': CC_values})

print(BC1)
print(CC1)

#merge는 합치다  node에 맞춰서 했다
new_data = pd.merge(BC1,CC1, on='node')
print(new_data)

#링크데이터에서 F노드 중 하나가 노드데이터에 어느 노드아이디에 들어간다면
# 그 노드아이디의 위도 경도를 가지고 오자

test_value = 9
#new_data의 노드값과 테스트 벨류랑 같은 곳의 위치에
print(float((new_data.loc[new_data['node'] == test_value])['BC']))