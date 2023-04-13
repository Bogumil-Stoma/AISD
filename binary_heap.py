class twoAry:
    def __init__(self):
        self.heap = []
        self.last = 0

    def push(self, val):
        self.heap.append(val)

        n = self.last
        parent = (n-1)//2
        while self.heap[parent] < self.heap[n] and parent > 0:
            self.heap[parent], self.heap[n] = self.heap[n], self.heap[parent]
            n = parent
            parent = (n-1)//2
        self.last += 1

    def __str__(self):
        return self.heap.__str__()

