"""
Checks if the conveyor belt can carry the packages based on motor count and total weight.
"""

MOTOR_CAPACITY = 12

### YOUR CODE HERE
motor_count = int(input("How many motors are carrying the packages?"))
total_package_weight = int(input("How many kg of packages do we expect?"))
total_capacity = motor_count * MOTOR_CAPACITY
if total_package_weight <= total_capacity:
    print("Yes! The conveyor belt can carry the packages.")
else:
    print("No. The conveyor belt cannot carry the packages.")
