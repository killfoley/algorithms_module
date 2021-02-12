# algorithm that returns the largest element in an array. 

arr = [20, 300, 16, 655, 8, 30, 20, 1]

def _biggest_(arr):
    biggest = arr[0]
    for n in range(1,len(arr)):
        if arr[n] > biggest:
            biggest = arr[n]
    return biggest

largest_val = _biggest_(arr)

print(f'The largest element in array: arr is {largest_val}')
