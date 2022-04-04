from collections import deque
from queue import LifoQueue

# Stack using lists
stack1 = []

stack1.append("Sahil")
stack1.append("Nitin")
stack1.append("Car")

# Pop method does LIFO - Last in, first out. These elements are not in the stack anymore.
for i in range(3):
    print(stack1.pop())

print(stack1)

# Stack using the deque class
# Instantiating stack2 as an object of the deque class
stack2 = deque()

stack2.append("Sahil")
stack2.append("Nitin")
stack2.append("Car")

for i in range(3):
    print(stack2.pop())

print(stack2)

# Stack using the LifoQueue class
# Instantiating stack3 as an object of the class
# Need to give max size as a parameter
stack3 = LifoQueue(maxsize=3)

stack3.put("Sahil")
stack3.put("Nitin")
stack3.put("Car")

for i in range(3):
    print(stack3.get())

print(stack3)