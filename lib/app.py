import ipdb

#DECORATORS IN PYTHON : FIRST CLASS FUNCTIONS IN PYTHON
def decorator_function(original_function):
    def wrapper_function():
        print(f"Wrapper executed before {original_function.__name__}")
        return original_function()
    return wrapper_function

@decorator_function
def display(): 
    print("Display function executed")
display()



# ipdb.set_trace()