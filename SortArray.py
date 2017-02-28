a = [1, 17, 30, 12, 100, 90, 900, 18]
a.sort()
print a

def sort(array=[1,17,30,12,100,90,900,18]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for b in array:
            if b < pivot:
                less.append(b)
            if b == pivot:
                equal.append(b)
            if b > pivot:
                greater.append(b)
        return sort(less)+equal+sort(greater)
    else:
        return array
print sort()