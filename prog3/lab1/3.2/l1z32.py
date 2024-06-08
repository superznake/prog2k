def SlowGuess(x,a,b):
    n=0
    for i in range(a,b+1):
        n+=1
        if i == x:
            print (f"Num is {i}, attemps:{n}")
            break


def FastGuess(x,a,b, n=0):
    n+=1
    if x == (a+b) // 2:
        print (f"Num is {(a+b)//2}, attemps:{n}")
    elif x<(a+b)//2:
        FastGuess(x,a,(a+b)//2,n)
    else:
        FastGuess(x,(a+b)//2,b,n)
    

while True:
    x = int(input("num: "))
    a = int(input("left: "))
    b = int(input("right: "))
    SlowGuess(x,a,b)
    FastGuess(x,a,b)