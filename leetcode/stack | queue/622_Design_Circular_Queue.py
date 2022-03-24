# 2022-03-23

# First Trial 
        
class MyCircularQueue(object):

    def __init__(self, k):
        self.c_queue = [-1 for _ in range(k)]
        self.head = 0
        self.tail = 0
        self.k = k   # k보단 size가 좀 더 직관적

    def enQueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.tail = 0
        else:
            if self.tail == self.k - 1:
                self.tail = 0
            else:
                self.tail += 1
        self.c_queue[self.tail] = value
        
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.c_queue[self.head] = -1
        if self.head == self.k - 1:
            self.head = 0
        else:
            self.head += 1
        return True
        

    def Front(self):
        if self.isEmpty():
            return -1
        return self.c_queue[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.c_queue[self.tail]
        

    def isEmpty(self):
        if self.head - self.tail == 1 or (self.head == 0 and (self.tail == self.k - 1 or self.tail == 0)):
            if self.c_queue[self.head] == -1:
                self.head = 0
                self.tail = 0
                return True
        return False
        

    def isFull(self):
        if self.head - self.tail == 1 or (self.head == 0 and self.tail == self.k - 1):
            if self.c_queue[self.head] != -1:
                return True
        return False
        

# =========================
# Other's solution
# Use size variable

class MyCircularQueue:
    def __init__(self, k):
        self.size = 0
        self.max_size = k
        self.t = [0] * k
        self.front = self.rear = -1

    def enQueue(self, value):
        if self.isFull(): return False
        if self.rear == -1:
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.t[self.rear] = value
        self.size += 1
        return True
    
    def deQueue(self, value):
        if self.isEmpty(): return False
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        if self.size == 0:
            self.front = self.rear = -1
        return True
        # another version
        if self.isEmpty(): return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self):
        return self.t[self.front] if not self.isEmpty() else -1
    
    def Rear(self):
        return self.t[self.rear] if not self.isEmpty() else -1

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.max_size


