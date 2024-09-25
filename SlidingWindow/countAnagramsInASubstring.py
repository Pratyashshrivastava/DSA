def countAnagram(s,t):
    ans = 0
    l = 0
    k = len(t)
    hashmap = {}
    for i in t:
        hashmap[i] = hashmap.get(i,0) +1

    count = len(hashmap)
    for r in range(len(s)):
        # if r-l+1==k:
        if s[r] in hashmap:
            hashmap[s[r]] -=1
            if hashmap[s[r]] ==0:
                count-=1
        if r-l+1>k:
            if s[l] in hashmap:
                hashmap[s[l]] +=1
            if hashmap[s[l]] ==1:
                count +=1
            l+=1
        if count ==0:
            ans+=1
        
    return ans

s = input()
t = input()
print(countAnagram(s,t))
