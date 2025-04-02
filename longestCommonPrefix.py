class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        prefix = ''
        for i in range(1,len(base)+1):
            prefix = base[:i]

            for j in range(len(strs)):
                if prefix != strs[j][:len(prefix)]:
                    return prefix[:-1]
        return prefix
