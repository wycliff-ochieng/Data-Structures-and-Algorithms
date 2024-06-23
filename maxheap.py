class MaxHeap:
    def __init__(self,items = []):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.floatUp(len(self.heap) - 1 )

    def push(self, data):
        self.heap.append(data)
        self.floatUp(len(self.heap) - 1 )

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
        
    def pop(self):
        if len(self.heap) > 2:
            self.swap(1, len(self.heap) - 1 )
            max = self.heap.pop()
            self.bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
            return max
        
    def swap(self,i , j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.floatUp(parent)

    def bubbleDown(self, index):
        left = index * 2
        right = index *2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.bubbleDown(largest)

    def __str__(self):
        return str(self.heap)
        
m = MaxHeap([95, 3, 21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())
