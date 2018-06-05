'''
Created on Jun 5, 2018

@author: shiwamsingh
'''
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue) 
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)   
queue.popleft()                 # The first to arrive now leaves

print(queue) 

queue.popleft()                 # The second to arrive now leaves

print(queue)                          # Remaining queue in order of arrival
