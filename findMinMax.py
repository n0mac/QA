a = [1, 17, 30, 44, 100, 90, 900, 18]

b = min(a)
c = max(a)
print b, c

d = 0
mini = a[d]
maxi = a[d]
while d < len(a):
    if a[d] < mini:
        mini = a[d]
    if a[d] > maxi:
        maxi = a[d]
    d = d + 1
print mini, maxi