from collections import deque

queue = deque()
queue.append(5)
queue.append(10)
queue.append(15)
print(queue)

while queue:
    print(queue.popleft())