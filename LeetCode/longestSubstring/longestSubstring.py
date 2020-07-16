def longSus(s):

    m={}
    longSub = 0
    left = 0
    right = 0
    n = len(s)

    while (right<n and left<n):
        el = s[right]
        if (el in m):
            left = max(left,m[el]+1)
        m[el] = right
        longSub = max(longSub,right-left+1)
        right += 1

    return longSub

if __name__=="__main__":
    list_string = "abcklmabcdedaghj"
    print(longSus(list_string))