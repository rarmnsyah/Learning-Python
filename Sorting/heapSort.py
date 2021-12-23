def heapsort(a):
    heapify(a, len(a))
    end = len(a)-1
    ans = 0
    while end > 0:
        print("swiftdown_heapsort")
        ans += 1
        a[end], a[0] = a[0], a[end]
        end -= 1
        sift_down(a, 0, end)
    print("ans:" , ans)

def heapify(a, count):
    start = int((count-2)/2)
    ans2 = 0
    while start >= 0:
        print("siftdown_heapify")
        ans2 += 1
        sift_down(a, start, count-1)
        start -= 1
    print("ans2:" , ans2)

def sift_down(a, start, end):
    root = start
    while (root*2+1) <= end:
        print("root", root)
        child = root * 2 + 1
        swap = root
        if a[swap] < a[child]:
            swap = child
        if (child + 1) <= end and a[swap] < a[child+1]:
            swap = child+1
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            root = swap
        else:
            return
        print(a)
        print("root", root)

anjay = [321,424,53,32,63,6,57]
# heapsort(anjay)
print(anjay)
heapsort(anjay)
print(anjay)
