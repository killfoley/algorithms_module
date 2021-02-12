# write an algorithm that returns a new array which is the reverse of the input.

arr = [3, 6, 9, 12, 15, 18, 21]

def reverse(arr):
    rev_arr = []
    for n in range(len(arr),0,-1):
        rev_arr.append(arr[n-1])
        n = n-1
    return rev_arr

back_arr = reverse(arr)

print(f'The reverse of your array is {back_arr}')