def lengthOfLongestSubstring(s: str) -> int:
    chars = [None] * 128  # O(n) search time
    left = right = 0
    res = 0
    while right < len(s):
        r = s[right]
        index = chars[ord(r)]
        if index != None and index >= left and index < right:
            left = index + 1
        res = max(res, right - left + 1)
        chars[ord(r)] = right
        right += 1
    return res

def lengthOfLongestSubstringFaster(s: str) -> int:
    # Use a dictionary instead for search - faster than a list = 2x faster
    sLen = len(s)
    charDict = {}  # Using a dictionary with O(1) search time
    maxLen = left = 0
    for right, ch in enumerate(s):
        if ch in charDict:
            newStart = charDict[ch] + 1
            if newStart > left:
                left = newStart  # Update the old index
        n = right - left + 1
        if n > maxLen:
            maxLen = n
        elif sLen - maxLen < left:
            return maxLen  # Cut the program early if there's no hope
        charDict[ch] = right
    return maxLen

def printAnswer(s:str):
    val = lengthOfLongestSubstring(s)
    val2 = lengthOfLongestSubstringFaster(s)
    print(val, val2)

s = "abcabcbb"
printAnswer(s)
s = "bbbbb"
printAnswer(s)
