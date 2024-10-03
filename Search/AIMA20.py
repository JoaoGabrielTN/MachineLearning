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

class BST:
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
            // TODO
            self.add(self.head, value)

    def _add(self, node, value): 
        if node.value >= value:
            if node.left == None:
                node.left = Node(value)
            else:
                self.add(node.left, value)
        else:
            if node.right == None:
                node.right = Node(value)
            else:
                add(node.right, value)

    def isEmpty(self):
        return self.__head == None

if __name__ == "__main__":
    tree = BST()
    tree.add(2)
    print(tree.head.value)
