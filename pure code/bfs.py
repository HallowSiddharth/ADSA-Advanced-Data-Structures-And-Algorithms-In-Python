#initialising a graph
graph={
    "A":["B","G"],
    "B":["C","D","E"],
    "C":[],
    "D":[],
    "E":["F"],
    "F":[],
    "G":["H"],
    "H":["I"],
    "I":[]
}

#BFS Implementation

def bfs(graph,node):
    queue=[]
    visited=[]
    queue.append(node)
    while queue!=[]:
        element=queue.pop(0)
        visited.append(element)
        queue.extend(graph[element])
    print(" ".join(visited))


#driver code to test it out
bfs(graph,"A") #from level 1
bfs(graph,"B") #from level 2
bfs(graph,"D") #from level 3
