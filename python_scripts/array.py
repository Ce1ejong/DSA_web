# Array Implementation (python_scripts/array.py)
# Basic operations: insert, delete, traverse

class ArrayOperations:
    """Represents array-like operations using Python's list."""
    def __init__(self, initial_list=None):
        self.array = initial_list if initial_list is not None else []

    def insert_element(self, index, value):
        """Inserts a value at a specific index."""
        try:
            self.array.insert(index, value)
            print(f"INSERT: Inserted {value} at index {index}")
        except IndexError:
            print(f"Error: Index {index} is out of bounds for insertion.")

    def delete_element(self, index):
        """Deletes the element at a specific index."""
        try:
            deleted_value = self.array.pop(index)
            print(f"DELETE: Deleted value {deleted_value} at index {index}")
        except IndexError:
            print(f"Error: Cannot delete. Index {index} is out of bounds.")

    def traverse(self):
        """Returns the current state of the array."""
        return self.array

# Example Usage (Output in website should reference this):
if __name__ == "__main__":
    arr_ops = ArrayOperations([10, 20, 30, 40])
    print(f"Initial Array: {arr_ops.traverse()}")
    
    # Insert
    arr_ops.insert_element(2, 50)
    print(f"Array after insertion: {arr_ops.traverse()}")
    
    # Delete
    arr_ops.delete_element(3)
    print(f"Array after deletion: {arr_ops.traverse()}")