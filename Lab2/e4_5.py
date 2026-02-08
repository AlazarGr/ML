m = [3.46871, 5.31916, 4.013449, 6.57686, 15.012678]

def func(x):
    return round(x,2)
def func1(x):
    return True if x > 5 else False

print(list(map(func,m)))

print(list(filter(func1,map(func,m))))