from basics.utility_classes import Calculate

calc = Calculate

#Factory Functions.
add = calc.get_method_by_operation("+", 2, 3)
#Printing the inner function
print(add)
#Priting the value return by the inner function
print(add())
