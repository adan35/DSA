


class Heap:
    
    def __init__(self, maxsize = 10):
        self.a = [None] * maxsize
        self.n = 0
        self.a[0] = 9999
        
    def insert(self, value):
        self.n += 1
        self.a[self.n] = value
        self.restoreUp(self.n)
        
    def restoreUp(self, i):
        k = self.a[i]
        iparent = i // 2
        while self.a[iparent] < k:
            self.a[i] = self.a[iparent]
            i = iparent
            iparent = i // 2
        self.a[i] = k
        
    def delete(self):
        maxValue = self.a[1]
        self.a[1] = self.a[self.n]
        self.n -= 1
        self.restoreDown(1)
        return maxValue
    
    def build_heap_top_down(self):
        for i in range(2, self.n):
            self.restoreUp(i)
            
    def build_heap_buttom_up(self):
        i = self.n // 2
        while i >= 1:
            self.restoreDown(i)
            i -= 1
    
    def restoreDown(self, i):
        k = self.a[i]
        left = 2 * i
        right = left + 1
        while right <= self.n:
            if k >= self.a[left] and k >= self.a[right]:
                self.a[i] = k
                return 
            else:
                if self.a[left] > self.a[right]:
                    self.a[left] = self.a[i]
                    i = left
                else:
                    self.a[right] = self.a[i]
                    i = right
        left = 2 * i
        right = left + 1
        # for even number of children
        if left == self.n and k < self.a[left]:
            self.a[left] = self.a[i]
            i = left
        self.a[i] = k
        