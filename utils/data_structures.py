"""Custom data structure implementations."""

class Stack:
    """Simple stack implementation using a list."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self._items = []
    
    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self._items.pop()
        raise IndexError("Pop from empty stack")
    
    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self._items[-1]
        raise IndexError("Peek from empty stack")
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self._items) == 0
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)
