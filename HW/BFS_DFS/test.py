import csv

f = open("BFS_DFS.csv", 'r')

reader = csv.reader(f)

data = []

for row in reader:
    data.append(row)

stack = data.pop()
print(type(stack))

print(data[len(data)-1])

data.append(stack)

print("Popped item: ")
print(data[len(data)-1])
