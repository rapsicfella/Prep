st = 'aabbDDDFFF'

def compress(st):
    count = 1
    ch = st[0]
    res = ''
    i = 1
    while i<len(st):
        if st[i] == st[i-1]:
            count +=1
        else:
            res = res+st[i-1]+str(count)
            count=1
        i+=1
    res = res+st[i-1]+str(count)
    return res

print(compress(st))