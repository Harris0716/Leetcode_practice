class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        key_str = strs[0]
        result = ""
        max_len = len(key_str)
        for i in range(max_len):
            for j in range(1, len(strs)):
                if i < len(strs[j]):
                    if strs[j][i] != key_str[i]:
                        return result
                    elif j == len(strs)-1:
                        result += key_str[i]
                else:
                    return result
        return result