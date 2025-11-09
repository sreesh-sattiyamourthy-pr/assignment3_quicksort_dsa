class Node:
    """Node for chaining in hash table."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """Hash table using chaining for collision resolution."""
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity

    def _hash(self, key):
        """Simple modular hashing function."""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Insert key-value pair."""
        index = self._hash(key)
        head = self.buckets[index]

        # Update value if key exists
        while head:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # Insert at beginning
        new_node = Node(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.size += 1

        # Resize if load factor exceeds threshold
        if self.load_factor() > 0.7:
            self._resize()

    def search(self, key):
        """Search for value by key."""
        index = self._hash(key)
        head = self.buckets[index]
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def delete(self, key):
        """Delete key-value pair."""
        index = self._hash(key)
        head = self.buckets[index]
        prev = None

        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.buckets[index] = head.next
                self.size -= 1
                return
            prev = head
            head = head.next

    def load_factor(self):
        """Compute load factor."""
        return self.size / self.capacity

    def _resize(self):
        """Double the capacity and rehash all keys."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0

        for bucket in old_buckets:
            head = bucket
            while head:
                self.insert(head.key, head.value)
                head = head.next

# Example usage
if __name__ == "__main__":
    ht = HashTable()
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("orange", 3)

    print("Search banana:", ht.search("banana"))
    ht.delete("banana")
    print("After delete, search banana:", ht.search("banana"))
