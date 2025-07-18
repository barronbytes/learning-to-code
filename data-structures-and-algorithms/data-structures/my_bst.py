from typing import Optional, List, Any


class BST:
    """
    Binary search tree class.
    
    Core Methods: insert(), search(), contains(), delete()
    Traversal Methods: inorder(), preorder(), postorder(), level_order()
    Utility / Helper Methods: get_min(), get_max(), height(), is_balanced(), size()
    """


    def __init__(self, value: Any) -> None:
        # Initialize a node with a value and empty left/right children
        self.value: Any = value
        self.left: Optional["BST"] = None
        self.right: Optional["BST"] = None


    def contains(self, value: Any) -> bool:
        # Check if a value exists in the BST
        result = False
        if value == self.value:
            result = True
        elif value < self.value and self.left:
            result = self.left.contains(value)
        elif value > self.value and self.right:
            result = self.right.contains(value)
        else:
            result = False
        return result

    
    def insert(self, value) -> None:
        # Insert a new value into the correct position in the BST
        if value == self.value:
            return
        elif value < self.value:
            if not self.left:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BST(value)
            else:
                self.right.insert(value)


    def delete(self, value: Any) -> Optional["BST"]:
        # Deletes a node from the BST and returns the updated subtree  
        if self is None:
            raise ValueError("List of values must not be empty.")
        elif value < self.value:
            if self.left:
                self.left = self.left.delete(value)  # recurse left and update pointer
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)  # recurse right and update pointer
        elif value == self.value:  # found the node to delete
            # CASE 1: Node has no children (leaf node)
            if self.left is None and self.right is None:
                return None  # node gets removed, parent sets this branch to None
            # CASE 2: Node has only a right child
            elif self.left is None:
                return self.right  # parent replaces this node with right child
            # CASE 3: Node has only a left child
            elif self.right is None:
                return self.left  # parent replaces this node with left child
            # CASE 4: Node has two children
            else:
                # Find in-order successor (leftmost node of right subtree)
                temp_successor = self.right
                while temp_successor.left:
                    temp_successor = temp_successor.left
                # Replace current node's value with the successor's value
                self.value = temp_successor.value
                # Delete the successor from the right subtree
                self.right = self.right.delete(temp_successor.value)
        return self


    def inorder(self) -> List[Any]:
        # Return the values using inorder traversal (left → root → right)
        values = []
        if self.left:
            values += self.left.inorder()
        values.append(self.value)
        if self.right:
            values += self.right.inorder()
        return values


    def preorder(self) -> List[Any]:
        # Return the values using preorder traversal (root → left → right)
        if self.value is None:
            return []
        nodes = [self.value]                        # visit root
        if self.left:
            nodes.extend(self.left.preorder())      # visit left subtree
        if self.right:
            nodes.extend(self.right.preorder())     # visit right subtree
        return nodes


    def postorder(self) -> List[Any]:
        # Return the values using postorder traversal (left → right → root)
        if self.value is None:
            return []
        nodes = []
        if self.left:
            nodes.extend(self.left.postorder())     # visit left subtree
        if self.right:
            nodes.extend(self.right.postorder())    # visit right subtree
        nodes.append(self.value)                    # visit root
        return nodes


    def get_min(self) -> Any:
        # Return the smallest value in the BST (leftmost node)
        current = self
        while current.left:
            current = current.left
        return current.value


    def get_max(self) -> Any:
        # Return the largest value in the BST (rightmost node)
        current = self
        while current.right:
            current = current.right
        return current.value


    @staticmethod
    def set_root(values: List[Any]) -> "BST":
        # Create a new BST from a list of values using the first value as root
        if not values:
            raise ValueError("List of values must not be empty.")
        root = BST(values[0])
        for val in values[1:]:
            root.insert(val)
        return root


    def height(self) -> int:
        # Return the height of the tree
        if self.value is None:
            return 0  # Edge case: empty node
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)


# --- Example Usage ---
values = [20, 10, 25, 5, 15, 30, 12]
root = BST.set_root(values)

print("Original data:", values)
print("Inorder Traversal:", root.inorder())
print("Preorder Traversal:", root.preorder())
print("Preorder Traversal:", root.postorder())
print("Minimum:", root.get_min())
print("Maximum:", root.get_max())


print("Tree Height (before deletions):", root.height())
root = root.delete(10)
print("Tree Height (after deletions):", root.height())
print("Inorder after deletion:", root.inorder())
print("Contains '1'?:", root.contains(1))
print("Contains '5'?:", root.contains(5))
