from bts import BinaryTreeSearch

bts = BinaryTreeSearch([1,2,10,4,5,11])
node = bts.search_iteratively(10)
print(node.value, node.left.value, node.right.value)

tree = bts.tree
print(tree.value)