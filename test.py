def yoimiya_dan_bioskop(bioskops, viewers, capacity):
    bioskops.sort()
    viewers.sort()
    
    view_id = 0 

    for bioskop in bioskops:
        maxed_bioskop = False
        cap = capacity

        while view_id < len(viewers) and viewers[view_id] <= bioskop and cap:
            cap -= 1
            view_id += 1

        if cap == 0: 
            maxed_bioskop = True

    if maxed_bioskop:
        ans = viewers[view_id-1]
    else:
        ans = bioskops[-1]

    booked = set(viewers)
    for i in range(ans, 0, -1):
        if i not in booked:
            return i

s, l, capacity = list(map(int, input().split()))
bioskops = list(map(int, input().split()))
viewers = list(map(int, input().split()))

print(yoimiya_dan_bioskop(bioskops, viewers, capacity))