class A:

    def show(self):
        print('A')

class B(A):

    def show(self):
        print('B')

class C(A):

    def show(self):
        print('C')

class D(B,C):

    def show(self):
        super().show() # B
        super(B,self).show() # C
        super(C,self).show() # A
        print('D') # D



def main():
    d = D()
    d.show()
    print(D.mro()) # method resolution order
    # [D,B,C,A]

if __name__ == '__main__':
    main()