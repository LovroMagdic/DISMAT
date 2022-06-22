from sys import maxsize
from itertools import permutations

def greedy(graph, n, a , b):
    min = 999999
    begin = 0
    end = 0
    rez = 0

    for i in range(n):
        for j in range(i+1,n,1):
            if(graph[i][j] < min) and (graph[i][j] != 0):
                begin = i
                end = j
                min = graph[begin][end]

    rez = rez + graph[begin][end]

    for i in range(n):
        graph[i][begin] = 0
    for i in range(n):
        graph[i][end] = 0

    for i in range(0,n-2,1):
        minimalLengthStart = 999999
        minimalIndexStart = 0
        minimalLengthEnd = 999999
        minimalIndexEnd = 0


        for i in range(n):
            if(graph[begin][i] < minimalLengthStart) and (graph[begin][i] != 0):
                minimalIndexStart = i
                minimalLengthStart = graph[begin][i]

        for i in range(n):
            if(graph[end][i] < minimalLengthEnd) and (graph[end][i] != 0):
                minimalIndexEnd = i
                minimalLengthEnd = graph[end][i]

        if (minimalLengthStart < minimalLengthEnd):
            rez = rez + minimalLengthStart
            begin = minimalIndexStart
            for k in range(n):
                graph[k][begin] = 0
        else:
            rez = rez + minimalLengthEnd
            end = minimalIndexEnd
            for k in range(n):
                graph[k][end] = 0

    for i in range(1, n + 1, 1):
        for j in range(1, n + 1, 1):
            if (i == j):
                graph[i - 1][j - 1] = 0
            elif (i < j):
                graph[i - 1][j - 1] = pow((a * (i)) + (b * (j)), 2) + 1
            elif (j < i):
                graph[i - 1][j - 1] = pow((a * (j)) + (b * (i)), 2) + 1

    rez = rez + graph[begin][end]
    return rez

def iscrpni(graph, s):
    vert = []
    for i in range(n):
        if i != s:
            vert.append(i)

    minimalPath = maxsize
    nextPerm = permutations(vert)
    for each in nextPerm:
        currWeight = 0
        k = s
        for each1 in each:
            currWeight += graph[k][each1]
            k = each1
        currWeight += graph[k][s]
        minimalPath = min(minimalPath, currWeight)
    return minimalPath


n = int(input("Unesi n > "))
a = int(input("Unesi a > "))
b = int(input("Unesi b > "))

graph = [[0 for i in range(n)] for j in range(n)]
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if (i == j):
            graph[i-1][j-1] = 0
        elif(i < j):
            graph[i-1][j-1] = pow((a*(i))+(b*(j)),2)+1
        elif(j < i):
            graph[i-1][j-1] = pow((a*(j))+(b*(i)),2)+1
s = 0

rezGreedy = greedy(graph, n , a, b)
rez1 = iscrpni(graph, s)
print("Pohlepni alogoritam nalazi ciklus duljine ", rezGreedy)
print("Iscrpni algoritam nalazi ciklus duljine ", rez1)

if(rezGreedy > rez1):
    print("Pohlepni alogoritam na ovom grafu ne daje optimalno rješenje!")

