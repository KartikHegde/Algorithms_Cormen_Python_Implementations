import Vertex
import Edges
import Algo


node1 = Vertex("A")
node2 = Vertex("B")
node3 = Vertex("C")

edge1 = Edges(1,node1,node2)
edge2 = Edges(1,node2,node3)
edge3 = Edges(0.1,node1,node3)

node1.adjlist.append(edge1)
node1.adjlist.append(edge2)
node2.adjlist.append(edge3)


vertexList = {node1,node2,node3}

algorithm = Algo()
algorithm.D_SPA(vertexList, node1)
algorithm.getShortestPath(node3)