import matplotlib
import matplotlib.pyplot as plt
import numpy as np

N = 100
c = list(np.random.randint(0,N,N))
x = range(N)
print('initial:',c)

# quicksort with pivot at end
def partition(array,low,pivindex):
    if pivindex - low > 0:
        pivot = array[pivindex]
        index = low
        for i in range(low,pivindex):
            if array[i] <= pivot:
                #swap
                temp = array[index]
                array[index] = array[i]
                array[i] = temp
                index += 1
  
        array[pivindex] = array[index]
        array[index] = pivot
    return array, index

def sort(array, low, high):
    piv = 0
    if low < high:
        array, piv = partition(array,low,high)
        
        #print('intermediate:', array)
        plt.clf()
        plt.bar(x,array)
        plt.bar(x[piv],array[piv],color='r')
        plt.pause(0.1)
        
        array = sort(array,low,piv-1)
        array = sort(array,piv+1,high)
    return array

def quicksort(seq):
    return sort(seq,0,len(seq)-1)

print('final:',quicksort(c))
plt.show()
