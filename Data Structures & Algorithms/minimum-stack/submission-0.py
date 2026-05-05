class MinStack:

    def __init__(self):
        self.data = []
        self.minEles = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.minEles: self.minEles.append(min(self.minEles[-1], val))
        else: self.minEles.append(val)
        

    def pop(self) -> None:
        self.data.pop()
        self.minEles.pop()
        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return self.minEles[-1]
        
