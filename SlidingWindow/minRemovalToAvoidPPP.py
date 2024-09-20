def min_removal(s):
    removals = 0
    i = 0

    while i<=len(s)-3:
        if s[i:i+3]=='ppp':
            removals +=1
            i+=1
        else:
            i+=1
    return removals
s = input()
print(min_removal(s))