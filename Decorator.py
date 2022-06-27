def smart_divide(func):
    def inner(a, b):
        print('I am going to divide', a, "and", b)
        if b == 0:
            print("Cannot divide !")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a/b

# tuong duong voi code
# def divide(a, b):
#     return a/b
# divide = smart_divide(divide)

print(divide(2, 5))
#print(divide(2,0))