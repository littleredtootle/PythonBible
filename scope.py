a = [1,2,3]

# Demonstrates global and local variables

def f1():
    a[0] = 5
    print(a)

def f2():
    a = 50 # local
    print(a)

f1()
f2()
print(a)
