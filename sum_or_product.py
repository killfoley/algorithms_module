#Script reads in an integer n from the user
#Offers to Sum 1 to n or multiply 1 to n

x = int(input("Please enter a positive integer: "))
_operation_ = str(input("Please enter s for sum or p for product of 1 ... n. "))

def _sumfunc_(x):
    _sum_ = 0
    for num in range(x):
        _sum_ += num
    print(f"The sum of all integers up to {x} is {_sum_}")

def _productfunc_(x):
    _product_ = 1
    for num in range(1, x+1):
        _product_ = _product_ * num
    print(f'The product of all integers up to {x} is {_product_}') 

if _operation_ == "s":
    _sumfunc_(x)

elif _operation_ == "p":
    _productfunc_(x)