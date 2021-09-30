import networkx as nx
import matplotlib.pyplot as plt
#실행은 Shift +f10
'''random 그래프(n,p)
n은 노드의 갯수
p는 노드들이 연결될 확률
complete 그래프는 노드들이 다 연결된거'''
G = nx.gnp_random_graph(100,0.45)
G1 = nx.scale_free_graph(200)
#nx.draw(G)

BC = nx.betweenness_centrality(G)
CC = nx.closeness_centrality(G)

deg = nx.degree(G)
print(BC)
print(CC)
print(deg)
nx.draw(G1,with_labels=1)
plt.show()
