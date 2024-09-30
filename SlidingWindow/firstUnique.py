def getUnique(arr):
    # seen = {}
    # for i in arr:
    #     seen[i] = seen.get(i,0) +1
    # for key,val in seen.items():
    #     if val==1:
    #         return key
    # return -1

    seen = [0]*max(arr)
    for i in arr:
        seen[i-1] +=1
    for _ in range(len(seen)):
        if seen[_] ==1:
            return arr[_]
    return -1
arr = list(map(int,input().split()))
print(getUnique(arr))