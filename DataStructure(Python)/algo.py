# Validation
# Maximum Node in left subtree should be less than root
# Minimum Node in right subtree should be greater than root
# Is the binary search tree balanced
# If unbalanced create a list and add root and its chilren to list
# and in preorder mode add each node to list
# steps for balancing
# if final index < initial index return false
# find mid-index
#
import math


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def pre_order(node, store_arr):
    if node is None:
        return
    store_arr.append(node.data)
    pre_order(node.left, store_arr)
    pre_order(node.right, store_arr)
    return store_arr


def in_order(node, store_arr):
    if node is None:
        return
    in_order(node.left, store_arr)
    store_arr.append(node.data)
    in_order(node.right, store_arr)
    return store_arr


def post_order(node, store_arr):
    if node is None:
        return
    post_order(node.left, store_arr)
    post_order(node.right, store_arr)
    store_arr.append(node.data)
    return store_arr


def bst_create(node, data):
    if node is None:
        node = Node(data)
        return node
    else:
        if data < node.data:
            node.left = bst_create(node.left, data)
        else:
            node.right = bst_create(node.right, data)
        return node


def max_node_finder(node):
    if node.right is None:
        return node
    else:
        max_node_finder(node.right)


def min_node_finder(node):
    if node.left is None:
        return node
    else:
        min_node_finder(node.left)


def height_of_tree(node):
    if node is None:
        return 0
    else:
        return 1 + max(height_of_tree(node.left), height_of_tree(node.right))


def validate_bst_limit(node, min_val, max_val):
    if node is None:
        return True
    elif node.data < min_val or node.data > max_val:
        return False
    else:
        return validate_bst_limit(node.left, min_val, node.data) and validate_bst_limit(
            node.right, node.data, max_val
        )


def validate_bst(node):
    if node is None:
        return True
    if node.left is not None and max_node_finder(node.left).data > root.data:
        return False
    if node.left is not None and min_node_finder(node.right).data < root.data:
        return False
    if not validate_bst(node.left) or not validate_bst(node.right):
        return False
    return True


def balanced(node):
    if node is None:
        return True
    if abs(height_of_tree(node.left) - height_of_tree(node.right)) > 1:
        return False
    return balanced(node.left) and balanced(node.right)


def collect_nodes(node, llist):
    if node is None:
        return None
    llist.append(node)
    collect_nodes(node.left, llist)
    collect_nodes(node.right, llist)
    return llist


def balance_tree(node_list, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    new_root = node_list[mid]
    new_root.left = balance_tree(node_list, left, mid - 1)
    new_root.right = balance_tree(node_list, mid + 1, right)
    return new_root


root = Node(50)

const = [
    17,
    44,
    90,
    47,
    80,
    53,
    43,
    1,
    55,
    82,
    62,
    11,
    4,
    54,
    63,
    9,
    5,
    40,
    6,
    68,
    94,
    86,
    66,
    96,
]
for i in const:
    bst_create(root, i)
# print(root.left.left.left.data)
root2 = Node(50)
bst_create(root2, 40)
bst_create(root2, 60)
bst_create(root2, 35)
bst_create(root2, 45)
bst_create(root2, 55)
bst_create(root2, 65)
temp = []
pre_order(root, temp)
print(temp)
print(validate_bst_limit(root, -math.inf, math.inf))
print(validate_bst_limit(root2, -math.inf, math.inf))
if not balanced(root):
    nodes = []
    collect_nodes(root, nodes)
    root = balance_tree(nodes, 0, len(nodes) - 1)
    print(pre_order(root, []))
    print(in_order(root, []))
    print(post_order(root, []))
    print(balanced(root))
