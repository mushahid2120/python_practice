'''
def firstN(N):
    for e in range(1,N+1):
        yield e;
it=iter(firstN(10))
for e firstN(10):
    print(e)


def fabN(N):
    x=-1
    y=1
    for e in range(1,N+1):
        z=x+y
        x=y
        y=z
        yield z;
f=fabN(10)
it=iter(f)
for e in it:
    print(e)


def sq(N):
    for e in range(1,N+1):
        yield e*e;
it=iter(sq(10))
for e in it:
    print(e)




l=[2,3,5,2,2,4,4,5,5,3]
it=iter(l)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
'''

l=[4,66,6]
it=iter(l)

while True:
    try:
        if next(it)%2:
            break
    except StopIteration:
        print("All the elements and even")
        break
