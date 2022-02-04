import networkx as nx
import re

#https://community.topcoder.com/stat?c=problem_statement&pm=2373

def readFile():
    adjacencyMatrix = []
    #Inside the file input your matrix
    with open("bridges.txt", "r") as f:
        lines = f.readlines()
    
    temp = ""
    for i in lines:
        #Extracting data from string and rmoving whitespaces
        temp = " ".join(re.split("[^0-9]*", i))
        temp = ''.join(temp.split())
        adjacencyMatrix.append(temp)
        
    return adjacencyMatrix

def createGraph(adjMatrix):
    g = nx.Graph()
    g.add_node(len(adjMatrix))
    
    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix)):
            if(adjMatrix[i][j]=="1"):
                g.add_edge(i+1,j+1)                       
    
    return g


def planRoute(bridges):
    graph = createGraph(bridges)

    pathList = list(nx.eulerian_circuit(graph,source=1))
    path = []

    for i in pathList:
        path.append(i[0]-1)

    path.append(0)

    print(path)


def main():
    planRoute(readFile())


if __name__ == "__main__":
    main()