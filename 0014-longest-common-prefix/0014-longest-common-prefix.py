class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = '0'
        for n in range(0, 200):
            prefix = '0'
            for i in range(len(strs)):
                a = strs[i][0:n + 1]
                if prefix == '0':
                    prefix = a
                elif prefix == a:
                    continue
                else:
                    return prefix[0:n]
                
        return prefix