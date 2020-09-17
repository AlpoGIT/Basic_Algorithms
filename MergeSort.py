c = [50,65,99,87,74,63,76,100,5]
print('initial:',c)

# merge a and b
def merge(a,b):
    'return ordered list, provided a and b are ordered'
    print('merge:',a,b)
    temp = []
    i,j = 0,0
    while (i < len(a)) and (j < len(b)):
        if a[i]>b[j]:
            temp.append(b[j])
            j += 1
        else:
            temp.append(a[i])
            i += 1
    return temp + a[i:] + b[j:]

def mergesort(c):
    L = len(c)
    mid = L//2
    while mid != 0:
        a = c[0:mid]
        b = c[mid:]
        d = merge(mergesort(a),mergesort(b))
        print('merged as:',d)
        print('-------------------------------------------')
        return d
    return c

print('final result:',mergesort(c))
