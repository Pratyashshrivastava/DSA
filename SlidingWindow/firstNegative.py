class sliding:
    def firstNegative(self, arr,k ):
        res = []
        l = 0
        r = 0
        neg = []
        while (r<len(arr)):
            if arr[r]<0:
                neg.append(arr[r])
            if r-l+1 ==k:
                if len(neg)==0:
                    res.append(0)
                else:
                    res.append(neg[0])
                    if arr[l] == neg[0]:
                        neg.pop(0)
                    l+=1
                
            r+=1
        return res

arr = list(map(int,input().split()))
k = int(input())
run = sliding()
print(run.firstNegative(arr,k))


# 1 -4 7 8 -9 -6 2 8 7
# op: -4 -4 -9 -9 -9 -6 0