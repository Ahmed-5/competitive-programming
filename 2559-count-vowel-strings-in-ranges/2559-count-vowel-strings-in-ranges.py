class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = 'aeiou'
        
        arr = [0]
        
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                arr.append(1)
            else:
                arr.append(0)
                
                
        for i in range(1, len(words)+1):
            arr[i] += arr[i-1]
            
        # print(*arr)
        
        ans = []
            
        for q in queries:
            s, e = q
            val = arr[e+1] - arr[s]
            ans.append(val)
            
        return ans