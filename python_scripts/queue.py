# Queue Implementation (python_scripts/queue.py)
# Basic operations: enqueue, dequeue, display
from collections import deque

class Queue:
    """Represents a FIFO Queue using Python's deque for efficiency."""
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        """Adds an item to the rear of the queue (O(1))."""
        self.items.append(item)
        print(f"ENQUEUE: Added {item}. Current Queue: {self.items}")

    def dequeue(self):
        """Removes and returns the item from the front of the queue (O(1))."""
        if self.is_empty():
            print("DEQUEUE: Queue is empty.")
            return None
        item = self.items.popleft()
        print(f"DEQUEUE: Removed {item}. Current Queue: {self.items}")
        return item
    
    def display(self):
        """Displays the elements in the queue from front to rear."""
        return list(self.items)

# Example Usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    q.dequeue()
    q.dequeue()
    
    print(f"Final Queue State: {q.display()}") # Output: [30]