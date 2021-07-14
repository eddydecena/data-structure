class Fenwick():
    def update(self, i, x):
        while i <= x:
            self.BIT[i-1] += x
            i += i & (-i)
    def query(self, i):
        s = 0
        while i > 0:
            s += self.BIT[i-1]
            i -= i & (-i)
        return s
    def __init__(self, l=[]):
        self.N = len(l)
        self.BIT = [0 for i in range(self.N)]
        for i in range(1,self.N+1):
            self.update(i, l[i-1])

if __name__ == '__main__':
    fenwick = Fenwick([1,2,3,4,5,6,7,8,9,10])
    print(fenwick.BIT)
    print(f'Result: {fenwick.query(5)}')
    
    print(fenwick.BIT)
    fenwick.update(5, 25)
    