import networkx as nx
import matplotlib.pyplot as plt


def show_graph(graph):
    
    graph_list = []
    for key in graph:
        for item in graph[key]:
            graph_list.append((key, item))

    # st.write(graph_list)
    
    fig, ax = plt.subplots()

    G = nx.DiGraph()
    G.add_edges_from(graph_list)
    
    pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    nx.draw_networkx_nodes(G, pos,
                           cmap=plt.get_cmap('jet'), 
                           node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=graph_list, edge_color='r', arrows=True)
    
    plt.show()
