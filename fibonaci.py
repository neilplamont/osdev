def fib( N: int) -> int:
        if (N <= 1):
            return N
        a = (N-1)
        b = (N-2)
        print(a+b)
        return (N-1)  + (N-2)

N=3
fib (3)