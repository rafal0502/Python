import one
print("TOP LEVEL two.py")
one.func()

if __name__ == '__main__':
    print("Two.py being run directyly")
else:
    print("two is being imported")
