def count7(N):
    '''
    N: a non-negative integer
    '''
    if N < 10:
        if N % 10 == 7:
            return 1
        else:
            return 0
    elif N >= 10:
        if N % 10 == 7:
            return count7(N//10) + 1
        else:
            return count7(N//10)



def dotProduct(listA, listB):
    '''
    Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32
    '''
    # Your code here
    sum = 0
    for idx in range(len(listA)):
        sum += (listA[idx] * listB[idx])
    return(sum)


def uniqueValues(aDict):
    '''
    Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)

    '''
    key_list = []
    value_list = []
    for key, value in aDict.items():
        value_list.append(value)
        key_list.append(key)

    target_idx = []
    for idx in range(len(value_list)):
        if value_list.count(value_list[idx]) == 1:
            target_idx.append(idx)

    target_keys = []
    for jdx in target_idx:
        target_keys.append(key_list[jdx])

    target_keys.sort()
    return(target_keys)

mydict = {1:3, 4:5, 7:9, 8:9}
# print(uniqueValues(mydict))
# print(uniqueValues({1: 1, 2: 1, 3: 1}))


def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """

    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# print(gcd(20,12))



def f(i):
    return i + 2
def g(i):
    return i > 5
L = [0, -10, 5, 6, -4]

def applyF_filterG(L, f, g):
    """
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    new_list = []
    for num in L:
        if g(f(num)):
            new_list.append(num)


    for i in L[:]:
        if i not in new_list:
            L.remove(i)

    if len(L) == 0:
        return -1
    else:
        return max(L)


print(applyF_filterG(L, f, g))
print(L)
