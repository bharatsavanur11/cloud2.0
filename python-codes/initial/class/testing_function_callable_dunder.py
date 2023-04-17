from basics.utility_classes import PersonService

## Testing Dunder call __call__ method which is automaticaly making class callable.
person = PersonService()
print(person('TestName1'))

# Should be present.
print(person.is_test('TestName1'))
# Should be absent.
print(person.is_test('TestName2'))
