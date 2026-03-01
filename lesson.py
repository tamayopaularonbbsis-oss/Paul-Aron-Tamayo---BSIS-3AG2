
import math
pi = math.pi

while True:
    print("=================================")
    radius_input = int(input("Enter radius: "))
    print("=================================")
    area_answer = pi * radius_input ** 2
    print(f'The area of the circle is: {area_answer:.2f}')
