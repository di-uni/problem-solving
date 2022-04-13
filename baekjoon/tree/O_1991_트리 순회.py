# First Trial
# Try to make tree structure... -> bst가 아니면 insert 비효율적이다.

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, node):
        if node.data == root.left.data:
            new_node = root.left
        elif node.data == root.right.data:
            new_node = root.right
        new_node = node
    
    def preorder(self, node):
        print(node.data, end="")
        if node.left != ".":
            self.preorder(node.left)
        if node.right != ".":
            self.preorder(node.right)
    


N = int(input())

data, left, right = input().split()
root = Node(data, left, right)
tree = Tree(root)

for _ in range(N - 1):
    data, left, right = input().split()



# Second Trial referred to other's solution
# tree를 dictionary로!

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
    
def preorder(node, tree):
    # print("hh")
    print(node.data, end="")
    if node.left != ".":
        preorder(tree[node.left], tree)
    if node.right != ".":
        preorder(tree[node.right], tree)

def inorder(node, tree):
    if node.left != ".":
        inorder(tree[node.left], tree)
    print(node.data, end="")
    if node.right != ".":
        inorder(tree[node.right], tree)
    
def postorder(node, tree):
    if node.left != ".":
        postorder(tree[node.left], tree)
    if node.right != ".":
        postorder(tree[node.right], tree)
    print(node.data, end="")
    
    
N = int(input())
tree = {}

for _ in range(N):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)

# print(tree)

preorder(tree['A'], tree)
print()
inorder(tree["A"], tree)
print()
postorder(tree["A"], tree)
print()

