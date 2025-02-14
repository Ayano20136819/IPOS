# a basic import
from greeter import Calculator

# use an alias - consider why might we do this?
# sometimes we only want to import what we need
# create a calculator class in the module
# use the new class to return a score to a user

calculator = Calculator(2, 7)
result = calculator.sum()
print(f"The sum is {result}")



git