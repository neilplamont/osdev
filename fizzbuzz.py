#for each multiple of 3 print fizz
#for each multiple of 5 print buzz


i=0
while i <=99:
    i=i+1
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz")
    elif i%3 == 0:
        print ("fizz")
    elif i%5 == 0:
        print ("buzz")
    else:
        print(i)


