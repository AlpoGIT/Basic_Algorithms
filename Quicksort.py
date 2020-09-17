c = [50,23,9,18,61,32]

def partition(seq,low,high):
    pivot = seq[high]
    index = low

    for i in range(low,high):
        if seq[i]<pivot:
            temp = seq[index]
            seq[index] = seq[i]
            seq[i] = temp
            index += 1
    seq[high] = seq[index]
    seq[index] = pivot
    return seq, index

def quicksort(seq,low,high):
    if low<high:
        seq, piv = partition(seq,low,high)
        seq = quicksort(seq, low, piv-1)
        seq = quicksort(seq,piv+1,high)
    return seq

print(quicksort(c,0,len(c)-1))
