import traceback

def main():
    try:
        a = 2
        b = int(input("b: "))
        c = a/b # erreur
        
        print(c)
    except ZeroDivisionError as e:
        print("=>",e)
        traceback.print_exc()


    # except TypeError as e:
    #     print("=>",e)
    #     traceback.print_exc()
    # except ValueError as e:
    #     print("=>",e)
    #     traceback.print_exc()
    except Exception as e:# intercepte Exception ou une de ses filles
        print("=>",e)
        traceback.print_exc()
    else:
        print("pas d'erreur")
    finally:
        print('finally')
    
    print('La fin')



if __name__ == '__main__':
    main()


