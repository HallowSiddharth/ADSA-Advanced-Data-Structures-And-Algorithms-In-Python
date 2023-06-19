import random


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        arr.remove(pivot)
        left = []
        right = []
        for i in arr:
            if i > pivot:
                right.append(i)
            else:
                left.append(i)
        return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([4, 2, 1, 2, 3, 84, 0, -213, 2, 4]))
