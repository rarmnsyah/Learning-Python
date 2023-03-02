output = []
n = 2
for i in range(n+1):
    temp = 0
    while(i>0):
        temp += 1 if i%2 == 1 else 0
        i = i//2
    print (i, temp, output)
    output.append(temp)
print(output)