import random
import timeit

global a
a = [random.randint(0, 11) for r in xrange(100)]
global b
b = [random.randint(0, 11) for r in xrange(100)]

def insertion_sort(a):
    for index in range(1, len(a)):

        value = a[index]
        i = index - 1
        while i >= 0:
            if value < a[i]:
                a[i + 1] = a[i]  # will move int in slot i to the right
                a[i] = value  # shifts value from left into slot i
                i = i - 1
            else:
                break


    t1 = timeit.Timer('[random.randint(0,11) for r in xrange(10)]', 'import random')
    t2 = timeit.Timer('[random.randint(0,11) for r in xrange(100)]', 'import random')
    t3 = timeit.Timer('[random.randint(0,11) for r in xrange(1000)]', 'import random')
    t4 = timeit.Timer('[random.randint(0,11) for r in xrange(10000)]', 'import random')
    t5 = timeit.Timer('[random.randint(0,11) for r in xrange(100000)]', 'import random')


    print ('insertion sort for an array size 10 took', (t1.timeit(100) ), 'secs')
    print ('insertion sort for an array size 100 took', (t2.timeit(100) ), 'secs')
    print ('insertion sort for an array size 1000 took', (t3.timeit(100) ), 'secs')
    print ('insertion sort for an array size 10000 took', (t4.timeit(100) ), 'secs')
    print ('insertion sort for an array size 100000 took', (t5.timeit(100) ), 'secs')



insertion_sort(a)

def merge(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c



def mergesort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)/2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])


t1 = timeit.Timer('[random.randint(0,11) for r in xrange(10)]', 'import random')
t2 = timeit.Timer('[random.randint(0,11) for r in xrange(100)]', 'import random')
t3 = timeit.Timer('[random.randint(0,11) for r in xrange(1000)]', 'import random')
t4 = timeit.Timer('[random.randint(0,11) for r in xrange(10000)]', 'import random')
t5 = timeit.Timer('[random.randint(0,11) for r in xrange(100000)]', 'import random')

print ('merge sort for an array size 10 took', (t1.timeit(100)), 'secs')
print ('merge sort for an array size 100 took', (t2.timeit(100) ), 'secs')
print ('merge sort for an array size 1000 took', (t3.timeit(100) ), 'secs')
print ('merge sort for an array size 10000 took', (t4.timeit(100)) , 'secs')
print ('merge sort for an array size 100000 took', (t5.timeit(100)) , 'secs')

merge(a,b)


def heap_sort(a):
    heapify(a, len(a))
    end = len(a) - 1
    while end > 0:
        a[end], a[0] = a[0], a[end]
        end -= 1
        sift_down(a, 0, end)
def heapify(a, count):
    start = int((count-2)/2)
    while start >= 0:
        sift_down(a, start, count-1)
        start -= 1

def sift_down(a, start, end):
    root = start
    while (root*2+1) <= end:
        child = root * 2 + 1
        swap = root
        if a[swap] < a[child]:
            swap = child
        if (child + 1) <= end and a[swap] < a[child+1]:
            swap = child+1
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            root = swap
        else:
            return
t1 = timeit.Timer('[random.randint(0,11) for r in xrange(10)]', 'import random')
t2 = timeit.Timer('[random.randint(0,11) for r in xrange(100)]', 'import random')
t3 = timeit.Timer('[random.randint(0,11) for r in xrange(1000)]', 'import random')
t4 = timeit.Timer('[random.randint(0,11) for r in xrange(10000)]', 'import random')
t5 = timeit.Timer('[random.randint(0,11) for r in xrange(100000)]', 'import random')

print ('heap sort for an array size 10 took', (t1.timeit(100) ), 'secs')
print ('heap sort for an array size 100 took', (t2.timeit(100)), 'secs')
print ('heap sort for an array size 1000 took', (t3.timeit(100) ), 'secs')
print ('heap sort for an array size 10000 took', (t4.timeit(100) ), 'secs')
print ('heap sort for an array size 100000 took', (t5.timeit(100) ), 'secs')

heap_sort(a)