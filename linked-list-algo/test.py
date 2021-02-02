from llist import SinglyLinkedList

llist = SinglyLinkedList()
print(f'Start Size: {llist.size}')

for i in range(20):
    print(f'Adding {i}')
    llist.head = i

llist.add_first(21)
llist.delete_last()

node = llist.head
while node is not None:
    print(node.value)
    node = node.next

print(f'End Size: {llist.size}')

print(f'head value: {llist.head.value}')
print(f'Tail value: {llist.tail.value}')

print(f'{"-" * 10} After value^2 {"-" * 10}')

llist.map(lambda x: x**2)

node = llist.head
while node is not None:
    print(node.value)
    node = node.next