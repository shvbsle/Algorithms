# Euler 79

"""
A common security method used for online banking is to ask the user for three random characters from a passcode. 
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
s->m->h
     ^
    /  \
  /     v
t->o->n->g
   ^  ^
    \ |
      r
      ^
      |
      w
"""

import sys

# unique logins
ip = list(set(sys.stdin.read().split('\n')))
# ip = """SMH,TON,RNG,WRO,THG""".split(',')

class node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.incoming = 0
        self.outgoing = 0
        self.children = []
    
    def show_out(self):
        print([x.value for x in self.children])
    

node_lookup = {}

# make the graph
for passcode in ip:
    prev = None
    for char in passcode:
        if char not in node_lookup:
            node_lookup[char] = node(char)
        if prev:
            prev.outgoing+=1
            prev.children.append(node_lookup[char])
            node_lookup[char].incoming += 1
        prev = node_lookup[char]

# find in and out degree
sources= {}
sinks = {}
for k,v in node_lookup.items():
    if v.outgoing == 0:
        sinks[k] = v
    if v.incoming == 0:
        sources[k] = v

stack = []

def DFS(node):
    global stack
    node.visited = True
    # print(node.value)
    if node.outgoing != 0:
        for n in node.children:
            if not n.visited:
                DFS(n)
    stack.append(node.value)

for starts in sources.keys():
    DFS(node_lookup[starts])

stack.reverse()
print(''.join(stack))
