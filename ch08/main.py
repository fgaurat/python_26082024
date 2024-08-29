class DivisionPar12Error(ArithmeticError):

    def __init__(self) -> None:
        super().__init__('Division par 12 !!!!!')

def divi(a,b):
    if b==12:
        e = DivisionPar12Error()
        raise e
    return a/b

def call_divi(a,b):
    
    try:
        print("OPEN FILE")
        r = divi(a,b)
    # except Exception as e:
    #     print("call_divi",e)
    #     raise e
    finally:        
        print("CLOSE FILE")
    return r


def main():
    try:
        r = call_divi(2,12)
        print(r)
    except DivisionPar12Error as e:
        print(e)


if __name__ == '__main__':
    main()