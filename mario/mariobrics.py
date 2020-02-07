import time

n = int(input('Height: '))

while (n < 1 or n > 10):
    n= int(input('Height: '))

#prints nxn bricks
for i in range(n):
    for j in range(n):
        print('#',end='')
    print()
    time.sleep(0.1)
print()
time.sleep(2)

#prints left-sided brick steps
for i in range(n):
    for j in range(i+1):
        print('#',end='')
    print()
    time.sleep(0.1)
print()
time.sleep(2)

#prints upsided brick steps
for i in range(n):
    for j in range(n-i):
        print('#',end='')
    print()
    time.sleep(0.1)
print()
time.sleep(2)


#prints right-sided bricks
for i in range(n):
    for j in range(n-i):
        print(' ', end='')
    for k in range(i+1):
        print('#', end='')
    print()
    time.sleep(0.1)
print()
time.sleep(2)


#prints dual bricks
for i in range(n):
    for j in range(n-i):
        print(' ', end='')
    for k in range(i+1):
        print('#', end='')
        time.sleep(0.1)
    for l in range(n):
        print(' ', end='')
    for m in range(i+1):
        print('#', end='')
        time.sleep(0.1)
    print()