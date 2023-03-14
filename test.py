def isSubsequence(s: str, t: str) -> bool:
    s = list(s)
    j = 0
    for i in t:
        if i == s[j]:
            j += 1
            if j == len(s):
                return True
    
    return False


print(isSubsequence('abc', 'hbgcc'))