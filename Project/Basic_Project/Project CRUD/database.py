data = {}

file1 = open('C:/Users/LENOVO/Template Program/Python/Project/Basic_Project/Project CRUD/database.txt', 'r')
stringData = file1.read().split('\n')
file1.close()

for i in range(len(stringData)):
    splitData = stringData[i].split(',')
    data[splitData[0]] = [splitData[1], splitData[2],splitData[3]]

def update2():
    file1 = open('C:/Users/LENOVO/Template Program/Python/Project/Basic_Project/Project CRUD/database.txt', 'w')
    file1.write('')
    file1.close()
    file1 = open('C:/Users/LENOVO/Template Program/Python/Project/Basic_Project/Project CRUD/database.txt', 'a')
    for i in data:
        file1.write(f'{i},{data[i][0]},{data[i][1]},{data[i][2]}\n')
    file1.close()


