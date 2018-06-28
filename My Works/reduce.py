from functools import reduce
def max(x,y):
    if x>y:
        return x
    else:
        return y
print(reduce(max,[1,4,3,6,2,8]))
