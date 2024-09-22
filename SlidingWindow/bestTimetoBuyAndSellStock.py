def stockI(price,n):
    left, right = 0,1
    maxP = 0
    while right<len(price):
        if price[left]<price[right]:
            profit = price[right]-price[left]
            maxP = max(maxP, profit)
        else:
            left = right
        right+=1
    return maxP

n = int(input())
price = list(map(int,input().split()))
print(stockI(price,n))