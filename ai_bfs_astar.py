#Best first search

n = int(input("Enter value : "))
gvalue = [[0 for i in range(n)] for j in range(n)]
print(gvalue)

e = int(input("No of edges? "))
print("Enter g values in adjacency matrix")
for k in range(0,e):
    i = int(input("Node 1? "))
    j = int(input("Node 2? "))
    gvalue[i][j] = int(input("g value? "))
    gvalue[j][i] = gvalue[i][j]

print(gvalue)
hvalue = []
for i in range(0,n):
    hvalue.append(int(input("h value for node" + str(i) + " ")))
    
source = int(input("Starting point?"))
destination = int(input("End point?"))

openlist = []
openlist.append(source)
closedlist = []
closedlist.append(source)

distance = 0
while destination not in closedlist:
    #add neghbours in open list 
    for j in range(0,n):
        if (gvalue[closedlist[-1]][j] != 0) and (j not in closedlist) and (j not in openlist):
            openlist.append(j)

    print("Openlist : " + str(openlist))
    #find minimum
    minimum = 999
    for i in openlist:
        if hvalue[i] < minimum:
            best = i
            minimum = hvalue[i]
    openlist.remove(best)
    if best not in closedlist :
        closedlist.append(best)
    distance = distance + hvalue[best]
    print("Closedlist : " + str(closedlist))
''' A* Algorithm goes here'''
# A * algorithm
n = int(input("Enter value : "))
e = int(input("No of edges? "))
print("Enter g values in adjacency matrix")
for k in range(0,e):
    i = int(input("Node 1? "))
    j = int(input("Node 2? "))
    gvalue[i][j] = int(input("g value? "))
    gvalue[j][i] = gvalue[i][j]

hvalue = []
for i in range(0,n):
    hvalue.append(int(input("h value for node" + str(i) + " ")))
    
source = int(input("Starting point?"))
destination = int(input("End point?"))

openlist = []
closedlist = []
closedlist.append(source)

distancefromsource = []
currentfvalue = []
for m in range(0,n):
    currentfvalue.append(0)
    distancefromsource.append(0)

best = source

while destination not in closedlist:
    
    #add neghbours in open list 
    for j in range(0,n):
        if (gvalue[closedlist[-1]][j] != 0) and (j not in closedlist) and (j not in openlist):
            openlist.append(j)

    print("Openlist: " + str(openlist))
    #update the distance from source
    for i in openlist:
        distancefromsource[i] = distancefromsource[best] + gvalue[best][i]

    #find f value
    for i in openlist:
        currentfvalue[i] = hvalue[i] + distancefromsource[i]

    #find minimum
    minimum = 999999
    for i in openlist:
        if currentfvalue[i] < minimum:
            best = i
            minimum = currentfvalue[i]

    openlist.remove(best)
    
    if best not in closedlist :
        closedlist.append(best)
    
    print("Closedlist : " + str(closedlist))

print("Distance required: " + str(distancefromsource[destination]))