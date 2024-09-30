def ksummax(arr,k):
    l = 0
    maxSum = float('-inf') 
    curr = 0
    for r in range(len(arr)):
        curr+=arr[r]
        if r-l+1>k:
            curr -= arr[l]
            l+=1
        if r-l+1==k:
            maxSum = max(curr,maxSum)

    return maxSum
k = int(input())
arr = list(map(int,input().split()))
print(ksummax(arr,k))