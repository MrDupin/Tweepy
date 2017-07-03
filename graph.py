import networkx as nx
from build_dict import Build


users = Build()
g = nx.DiGraph()
g.add_nodes_from(users.values())

for u_id, u_nm in users.items():
    f = open("ids/{}".format(u_id), 'r')
    followers = [l.strip() for l in f.readlines()]
    f.close()
    [g.add_edge(users[follower], u_nm) for follower in followers if follower in users.keys()]
    if len(followers) >= 49999:
        print(u_id, len(followers))


for n in g:
    print(len(g.in_edges(n)), len(g.out_edges(n)))


print("\nStrongly Connected Components:\n")

s_components = nx.strongly_connected_components(g)
for c in s_components:
    print(c)

print("\nWeakly Connected Components:\n")

w_components = nx.weakly_connected_components(g)
for c in w_components:
    print(c)
