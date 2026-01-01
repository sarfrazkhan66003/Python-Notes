from collections import deque

def reverse_queue(q):
    stack=[]
    
    #push elements from the queue to stack
    while q:
        stack.append(q.popleft())
    
    #pop elements from the stack to the queue
    
    while stack:
        q.append(stack.pop())
    return q    

queue= reverse_queue(deque([1,2,3,4,5]))
print(queue)            