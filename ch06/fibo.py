# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result




def main():
    
    
    print("__name__", __name__)  # dunder (double underscore) : dunder name

    print("TEST")
    fib(12)
    print(fib2(12))
    print("END TEST")


if __name__ == "__main__": # éxécution
    main()

    