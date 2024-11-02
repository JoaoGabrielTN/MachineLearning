from abc import ABC, abstractmethod

class Node:
    def __init__(self, v):
        self.__left = None
        self.__right = None
        self.__value = v

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, n) -> None:
        self.__left = n

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, n) -> None:
        self.__right = n

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v

class BST():
    def __init__(self):
        self.__head = None

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, new_head):
        self.__head = new_head

    def add(self, value):
        if self.isEmpty():
            self.head = Node(value)
        else:
            self._add(self.head, value)

    def _add(self, node, value): 
        if node.value >= value:
            if node.left == None:
                node.left = Node(value)
            else:
                self._add(node.left, value)
        else:
            if node.right == None:
                node.right = Node(value)
            else:
                self._add(node.right, value)

    def isEmpty(self):
        return self.__head == None

class TreeIterator(ABC):
    @abstractmethod
    def walk(self) -> None:
        pass

    @abstractmethod
    def search(self, value):
        pass

class DFSIterable(TreeIterator):
    def __init__(self, agregated):
        self.agregated = agregated

    def walk(self): 
        stack = [self.agregated.head]
        while stack:
            curr = stack.pop(-1)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            print(curr.value, end=" ")


    def search(self, v): 
        stack = [self.agregated.head]
        while stack:
            curr = stack.pop(-1)
            if curr.value == v:
                return curr

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return None

class IDFSIterator(TreeIterator):
    def __init__():
        pass

if __name__ == "__main__":
    tree = BST()
    values = [1, 5, 10, 3, 6, 7]
    for i in values:
        tree.add(i)

    iterator = DFSIterable(tree)
    iterator.walk()
