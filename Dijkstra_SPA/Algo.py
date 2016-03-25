import heapq

def D_SPA(self,virtexlist, startVertex):

    queue = []
    startVertex.minDistance = 0
    heapq.heappush(queue,startVertex)


    while len(queue) > 0 :
        actualVertex = heapq.heappop(queue)

        for edge in actualVertex.adjlist:
            u = edge.startVertex
            v = edge.targetVertex

            newDistance = u.minDistance + edge.weight


            if newDistance < v.minDistance:
                v.predecessor = u
                v.minDistance = newDistance
                heapq.heappush(queue,v)

def getShortestPath ( self,targetVertex):
    print ("Shortest path to target is : ", targetVertex.minDistance)

    node = targetVertex

    while node is not None :
        print ("%s -> "% node.name)
        node = node.predecessor




