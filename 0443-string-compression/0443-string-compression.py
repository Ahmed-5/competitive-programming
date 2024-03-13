class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        current = chars[0]
        n = len(chars)
        ind = 0
        for _ in range(n):
            i = chars.pop(0)
            if i == current:
                count += 1
            else:
                chars.append(current)
                if count > 1:
                    for c in str(count):
                        chars.append(c)
                current = i
                count = 1
                
        chars.append(current)
        if count > 1:
            for c in str(count):
                chars.append(c)
                
        print(*chars)
        return len(chars)
        