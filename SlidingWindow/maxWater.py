def maxWater(arr):
    l = 0
    r = len(arr)-1
    maxArea = 0
    while l<r:
        maxArea = max(maxArea, (r-l)*min(arr[l],arr[r]))
        if arr[l]<arr[r]:
            l+=1
        else:
            r-=1
    return maxArea

arr = list(map(int,input().split()))
print(maxWater(arr))