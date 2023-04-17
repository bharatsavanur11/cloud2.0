from basics.utility_classes import PersonService

# To Determine if an object/class/abmda is callable

person = PersonService()
# is person callable
print(callable(person))

## __init__ and __call__ are not callable as they are internal and cannot be called externally.

# Calling Manually defined objects.
print(callable(person.sort_scientist))
