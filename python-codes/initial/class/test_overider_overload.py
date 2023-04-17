from basics.utility_classes import Calculate
from basics.utility_classes import PersonService

# Calculate contains a method to calculate are/volum.

cal = Calculate
svc = PersonService

# Calculate volume for 3 sides
print(cal.hyper_volume(1, 2, 3))

# Calculate volume for 4 sides
print(cal.hyper_volume(1, 2, 3, 4))

print(svc.build_person_info('Bharat', age=33, surname='Savanur'))
