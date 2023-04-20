class twoAry:
    def __init__(self):
        self.heap = []
        self.last = 0

    def push(self, val):
        self.heap.append(val)

        n = self.last
        parent = (n-1)//2
        while self.heap[parent] < self.heap[n] and parent >= 0:
            self.heap[parent], self.heap[n] = self.heap[n], self.heap[parent]
            n = parent
            parent = (n-1)//2
        self.last += 1

    def __str__(self):
        return self.prepare_string()

    def pop(self):
        first = self.heap[0]
        self.last -= 1
        v = self.heap.pop()
        i = 0
        j = 1
        while j < self.last:
            if (j+1 < self.last):
                t = j
                maxH = self.heap[j]
                for k in range(min(1,self.last-j-1)):

                    if (self.heap[j+1+k] > self.heap[j+k] and self.heap[j+1+k] > maxH):
                        maxH = self.heap[j+1+k]
                        t = j+k+1
                j = t
            if v >= self.heap[j]:
                break
            self.heap[i] = self.heap[j]
            i = j
            j = 2*j + 1
        self.heap[i] = v
        return



    def prepare_string(self):
        j = 0
        k = 1
        text = []
        res = ''
        for i in range(self.last):
            text.append(str(self.heap[i]))
            if i == j:
                res += '       '.join(text).center(50)+'\n'+ '       '.join(['/  \\']*(2**(k-1))).center(50)
                res += '\n'
                text = []
                j = 2**(k) + j
                k+=1
        res += '       '.join(text).center(10)
        res += '\n'
        text = []
        return res

class threeAry:
    def __init__(self):
        self.heap = []
        self.last = 0

    def push(self, val):
        self.heap.append(val)

        n = self.last
        parent = (n-1)//3
        while self.heap[parent] < self.heap[n] and parent >= 0:
            self.heap[parent], self.heap[n] = self.heap[n], self.heap[parent]
            n = parent
            parent = (n-1)//3
        self.last += 1

    def pop(self):
        first = self.heap[0]
        self.last -= 1
        v = self.heap.pop()
        i = 0
        j = 1
        while j < self.last:
            if (j+1 < self.last):
                t = j
                maxH = self.heap[j]
                for k in range(min(2,self.last-j-1)):

                    if (self.heap[j+1+k] > self.heap[j+k] and self.heap[j+1+k] > maxH):
                        maxH = self.heap[j+1+k]
                        t = j+k+1
                j = t
            if v >= self.heap[j]:
                break
            self.heap[i] = self.heap[j]
            i = j
            j = 3*j + 1
        self.heap[i] = v
        return first

    def __str__(self):
        return self.prepare_string()

    def prepare_string(self):
        j = 0
        k = 1
        text = []
        res = ''
        for i in range(self.last):
            text.append(str(self.heap[i]))
            if i == j:
                res += '       '.join(text).center(50)+'\n'+ '       '.join(['/ | \\']*(3**(k-1))).center(50)
                res += '\n'
                text = []
                j = 3**(k) + j
                k+=1
        res += '       '.join(text).center(10)
        res += '\n'
        text = []
        return res

class fourAry:
    def __init__(self):
        self.heap = []
        self.last = 0

    def push(self, val):
        self.heap.append(val)

        n = self.last
        parent = (n-1)//4
        while self.heap[parent] < self.heap[n] and parent >= 0:
            self.heap[parent], self.heap[n] = self.heap[n], self.heap[parent]
            n = parent
            parent = (n-1)//4
        self.last += 1

    def pop(self):
        first = self.heap[0]
        self.last -= 1
        v = self.heap.pop()
        i = 0
        j = 1
        while j < self.last:
            if (j+1 < self.last):
                t = j
                maxH = self.heap[j]
                for k in range(min(3,self.last-j-1)):

                    if (self.heap[j+1+k] > self.heap[j+k] and self.heap[j+1+k] > maxH):
                        maxH = self.heap[j+1+k]
                        t = j+k+1
                j = t
            if v >= self.heap[j]:
                break
            self.heap[i] = self.heap[j]
            i = j
            j = 4*j + 1
        self.heap[i] = v
        return first


    def __str__(self):
        return self.prepare_string()

    def prepare_string(self):
        j = 0
        k = 1
        text = []
        res = ''
        for i in range(self.last):
            text.append(str(self.heap[i]))
            if i == j:
                res += '       '.join(text).center(100)+'\n'+ '       '.join(['/    /    \\    \\']*(4**(k-1))).center(100)
                res += '\n'
                text = []
                j = 4**(k) + j
                k+=1
        res += '       '.join(text).center(10)
        res += '\n'
        text = []
        return res