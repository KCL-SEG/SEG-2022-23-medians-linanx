"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
numbers.sort()
print(f'Your sorted list: {numbers}')

if len(numbers)%2 == 0:
    m1 = (len(numbers)//2)-1
    m2 = len(numbers)//2
    print((numbers[m1]+numbers[m2])/2)
else:
    length = ((len(numbers)+1)//2)
    print(numbers[length-1])
