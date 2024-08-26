# Fibonacci series:
# the sum of two elements defines the next

a, b = 0, 1

while a < 10:
    # breakpoint()
    print(a)
    a, b = b, a+b # a=0,b=1
    