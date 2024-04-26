class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.index = 0
        

    def visit(self, url: str) -> None:
        while len(self.hist)>0 and len(self.hist)-1 > self.index:
            self.hist.pop()
        self.hist.append(url)
        self.index += 1
        # print(self.index, self.hist)
        

    def back(self, steps: int) -> str:
        self.index = max(0, self.index-steps)
        # print(self.index, self.hist)
        return self.hist[self.index]
            
        

    def forward(self, steps: int) -> str:
        n = len(self.hist)
        self.index = min(n-1, self.index+steps)
        # print(self.index, self.hist)
        return self.hist[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)