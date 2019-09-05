import csv

f = open("BFS_DFS.csv", 'r')

reader = csv.reader(f)

data = []

#for row in reader:
#    data.append(row)
[next(reader) for row in range(0, 5)]:
    data.append(row)

stack = data.pop(3)

print(data)

#print(data[len(data)-1])

#data.append(stack)

#print("Popped item: ")
#print(data[len(data)-1])
