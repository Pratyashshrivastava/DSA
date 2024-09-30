def moveZeros(n,arr):
    non = []
    for i in arr:
        if i!=0:
            non.append(i)
    for _ in range(len(arr)-len(non)):
        non.append(0)
    return non
    # return " ".join(str(i) for i in nonZeros)
n = int(input())
arr = list(map(int,input().split()))
print(moveZeros(n,arr))