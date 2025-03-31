class KeyValueStore:
    def __init__(self):
        # Permanent storage for key-value pairs
        self.permanent_store = {}
        # Stack to manage nested transactions
        self.transaction_stack = []
        # Marker for deleted keys
        self.DELETED = "<DELETED>"

    def set(self, key, value):
        if self.transaction_stack:
            # Store in the latest transaction hashmap
            self.transaction_stack[-1][key] = value
        else:
            # Directly update permanent store if no active transaction
            self.permanent_store[key] = value

    def get(self, key):
        # Check transactions stack from top to bottom
        for transaction in reversed(self.transaction_stack):
            if key in transaction:
                return None if transaction[key] == self.DELETED else transaction[key]
        # Check the permanent store
        return self.permanent_store.get(key)

    def delete(self, key):
        if self.transaction_stack:
            # Mark key as deleted in the latest transaction
            self.transaction_stack[-1][key] = self.DELETED
        elif key in self.permanent_store:
            # Delete directly from the permanent store if no active transaction
            del self.permanent_store[key]

    def begin(self):
        # Start a new transaction by pushing an empty hashmap onto the stack
        self.transaction_stack.append({})

    def commit(self):
        if not self.transaction_stack:
            raise RuntimeError("No active transaction to commit")
        
        # Merge top transaction into the previous one or permanent store
        current_transaction = self.transaction_stack.pop()
        if self.transaction_stack:
            # Merge into the next transaction down
            for key, value in current_transaction.items():
                if value == self.DELETED:
                    self.transaction_stack[-1][key] = self.DELETED
                else:
                    self.transaction_stack[-1][key] = value
        else:
            # Merge into the permanent store
            for key, value in current_transaction.items():
                if value == self.DELETED:
                    self.permanent_store.pop(key, None)
                else:
                    self.permanent_store[key] = value

    def rollback(self):
        if not self.transaction_stack:
            raise RuntimeError("No active transaction to rollback")
        # Discard the latest transaction
        self.transaction_stack.pop()

# Testing the implementation
if __name__ == "__main__":
    kv_store = KeyValueStore()

    # Basic operations
    kv_store.set("a", 10)
    print(kv_store.get("a"))  # Output: 10
    kv_store.delete("a")
    print(kv_store.get("a"))  # Output: None

    # Transaction operations
    kv_store.begin()
    kv_store.set("b", 20)
    print(kv_store.get("b"))  # Output: 20
    kv_store.rollback()
    print(kv_store.get("b"))  # Output: None

    # Nested transactions
    kv_store.begin()
    kv_store.set("c", 30)
    kv_store.begin()
    kv_store.set("c", 40)
    print(kv_store.get("c"))  # Output: 40
    kv_store.rollback()
    print(kv_store.get("c"))  # Output: 30
    kv_store.commit()
    print(kv_store.get("c"))  # Output: 30

    # Error handling
    try:
        kv_store.rollback()
    except RuntimeError as e:
        print(e)  # Output: No active transaction to rollback
