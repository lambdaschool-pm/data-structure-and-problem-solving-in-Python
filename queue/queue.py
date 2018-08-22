class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, item):
        # add item to the end of the list
        self.storage.append(item)

    def dequeue(self):
        if(len(self.storage) > 0):
            return self.storage.pop(0)
        else:
            return None

    def len(self):
        return len(self.storage)
