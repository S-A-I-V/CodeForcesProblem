class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        n = len(s)
        swaps = 0
        
        for i in range(n):
            for j in range(1, n):
                if s[j-1] == '1' and s[j] == '0':
                    s[j-1], s[j] = s[j], s[j-1]
                    swaps += 1
        
        return swaps
        