pattern = "abbab"
s = "dog cat cat dog dog"
s = s.split(' ')

# print(s, pattern.split(''))
def anjay(pattern, s):
    if(len(pattern) != len(s)): return (False)

    temp = {}

    for i, j in zip(pattern, s):
        if i in temp:
            if temp[i] != j:
                return False
        elif j in temp.values():
            return False
        else:
            temp[i] = j
    return True

print(anjay(pattern, s))
        





