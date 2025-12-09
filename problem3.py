#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

num = int(input("Enter a number: "))

if 0 < num < 10:
    total = 0
    g = 0
    for i in range (num):
        g = 10**i
        total += g
        sum = total
    print(f"the sum of the series is {sum}")
else:
    pass

#yoku wakaran