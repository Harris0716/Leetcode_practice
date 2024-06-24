class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        max_len = len(prefix)
        for j in range(1, len(strs)):
            while prefix[:max_len] != strs[j][:max_len]:
                max_len -= 1
                if max_len == 0:
                    return ""
        return prefix[:max_len]