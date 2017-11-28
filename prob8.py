def fibonacci(num):
    n1 = 0
    n2 = 1
    for i in range(num):
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
numm=input("Enter number of elements in series:")
num=int(numm)
fibonacci(num)
