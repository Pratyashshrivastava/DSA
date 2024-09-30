def alternateNos(arr):
    a,b = [],[]
    for i in arr:
        if i>=0:
            a.append(i)
        else:
            b.append(i)
    # a -> technical(+ve)
    # b -> creative(-ve)
    res = []
    
    t,c = 0,0
    n,m = len(a),len(b)

    while t<n or c<m:
        if c<m:
            res.append(b[c])
            c+=1
        if t<n:
            res.append(a[t])
            t+=1
    return res

arr = list(map(int,input().split()))
print(alternateNos(arr))