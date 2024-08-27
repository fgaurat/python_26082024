# import fibo as fb
# fb.fib(12)
# l = fb.fib2(12)
# print(l)

from fibo import fib as ffib
import sys
# sys.path.append("/Users/fgaurat/local_dev/formations/python_26082024")
# import ledossier.lemodule
from ..ledossier import lemodule

def fib(a):
    print("Fib", a)


def main():
    fib(12)
    ffib(12)
    print(sys.path)
    ledossier.lemodule.f()


if __name__ == '__main__':
    main()
