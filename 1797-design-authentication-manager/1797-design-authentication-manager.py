class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = dict()
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            if self.tokens[tokenId] + self.ttl > currentTime:
                self.tokens[tokenId] = currentTime
            else:
                del self.tokens[tokenId]
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        num = 0
        
        for i in self.tokens:
            if self.tokens[i] + self.ttl > currentTime:
                num += 1
                
        return num
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)