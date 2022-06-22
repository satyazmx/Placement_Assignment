# Example 1
def function1(funct):
    def wrapper():
        print("Started")
        funct()
        print("Ended")
    return wrapper

def function():
    print("Hello")

#funct1(function)()
function_call = function1(function)
function_call()

'''
O/p=>   Started
        Hello
        Ended
'''

# Example 2
def division(a,b):
    print("Result=",a/b)
    
def updated_division(func):
    
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

division = updated_division(division)# Decorators adds extra features to our existing function
division(2,4)
# O/p: 2.0


