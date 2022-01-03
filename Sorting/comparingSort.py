def findSmallest(array):
    smallest = array[0]
    smallestIndex = 0
    for i in range(len(array)):
        if array[i] < smallest:
            smallestIndex = i
            smallest = array[i]
    return smallestIndex

def selectionSort(array:list()):
    sortedArray = []
    for i in range(len(array)) :
        smallest = findSmallest(array)
        sortedArray.append(array.pop(smallest))
    return sortedArray

array = [12,3,14,1,12,31,24,1,1,51,3,12,1,2,1,23,12,41,4]
print(array)
print(selectionSort(array))
