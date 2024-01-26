def myrange2(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    res = list()
    while start < stop:
        res.append(start)
        start += step
    return res

def myrange3(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    while start < stop:
        yield start
        start += step

for x in myrange2(10, 30, 3):
    print(x, end=' ')
print()
for x in myrange3(10, 30, 3):
    print(x, end=' ')
print()