s = input()

vowels = ['a', 'i', 'u', 'e', 'o']
temp = [i for i in s if i.lower() in vowels]
print(temp)
news = ''
for i in s:
    if i.lower() in vowels:
        news += temp.pop()
    else :
        news += i
    
print(news)


        