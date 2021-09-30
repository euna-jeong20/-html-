import pandas as pd

nodes = pd.read_csv('Daegu_node_1.csv')
links = pd.read_csv('Daegu_link_1.csv')

nodes = nodes[['NODE_ID','NODE_NAME','STNL_REG','Y','X']]
G_link = links[['F_NODE','T_NODE']] #F와 T를 잇는 링크만 가져오겠다.

print(nodes)

G1 = list(links['F_NODE'])
G2 = list(links['T_NODE'])

G3 = G1 +G2
print(len(G3))      #len은 길이

G3set = set(G3)     #set이 순서정렬과 중복제거
print(len(G3set))

print(len(nodes['NODE_ID']))

