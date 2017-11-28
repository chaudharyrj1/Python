for i in range(1,51):
    if(i%3==0):
       if(i%5==0):
           print("fizzbuzz")
           continue
       else:
           print("fizz")
           continue
    if(i%5==0):
        print("buzz")
        continue
    print(i)
