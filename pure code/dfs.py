#initialising this graph
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

#DFS Code

def dfs(graph,node):
    visited=[]
    stack=[]
    stack.append(node)

    while stack!=[]:
        element = stack.pop(-1)
        visited.append(element)
        stack.extend(graph[element][::-1])
        """ we are goiing to be looking at elements from left to right, stack always pops from last
        so we are reversing the connected nodes, so that the left most element appears on the top 
        of the stack"""

    print(" ".join(visited))


#driver code

print("Searching from A:")
dfs(graph,"A")
print("\nSearching from B:")
dfs(graph,"B")
print("\nSearching from G:")
dfs(graph,"G")


