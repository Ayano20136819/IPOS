'''Considering reuse (modularisation)
when creating python programs'''
def greet():
    print("Hello, World!")

# create a calculator class and re-use this by instantiating it in the main.py
# So as not to contaminate your global namespace, it is good practice to use a main function.
# so that we can reuse our code as both a module and a script
# we can use an if statement to ensure that some code is only executed when name is __main__
# module name when imported
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2





    # above is __main__ when running directly
    # only called when a script