def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func


# def func_needs_decorator():
#     print("THIS FUNCTION IS IN NEED OF A DECORATOR!")


#func_needs_decorator = new_decorator(func_needs_decorator)

    # DEKORATOR NIŻEJ TO TO SAMO CO TO WYWOŁANIE WYŻEJ

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")



func_needs_decorator()
