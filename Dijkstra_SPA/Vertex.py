import sys

class Vertex (object):
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.adjlist = []
        self.minDistance = sys.maxsize
        self.predece = None

#
    def __cmp__(self, nextvertex):
        return self.cmp(self.minDistance,nextvertex.minDistance)

    def __lt__(self,other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority


