class HeapMap:
    def __init__(self):
        self.heap = []


    def _left_index(self, index):
        return 2*index + 1

    def _right_index(self, index):
        return 2*index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def swap_child(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _insert_child(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self.swap_child(current, self._parent(current))
            current = self._parent(current)

    def sink_down(self, index):
        size = len(self.heap)
        while True:
            largest = index
            left = self._left_index(index)
            right = self._right_index(index)

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.swap_child(index, largest)
            index = largest

            
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)

        return max_value
    
    @staticmethod
    def find_kth_smallest(nums, k):
        max_heap = HeapMap()

        if k > len(nums):
            return None
        for num in nums:
            max_heap._insert_child(num)
            if len(max_heap.heap) > k:
                max_heap.remove()
        
        return max_heap.remove()
    
my_heap = HeapMap()
my_heap._insert_child(7)
my_heap._insert_child(5)
my_heap._insert_child(3)
my_heap._insert_child(1)
my_heap._insert_child(9)
my_heap._insert_child(4)
my_heap._insert_child(6)

numslist = [7,5,3,1,9,4,6]
print(my_heap.find_kth_smallest(numslist, 8))