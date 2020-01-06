'''
URL: https://www.hiredintech.com/classrooms/algorithm-design/lesson/76/task/27

Task: Digit sum
Implement a program, which given an integer n, computes the sum of its digits.

If a negative number is given, the function should work as if it was positive.

For example, if n is 1325132435356, the digit's sum is 43. If n is -10, the sum is 1 + 0 = 1.

In the test cases for this task we will have that -2^63 < n < 2^63.

Test examples
10	=> 1
2	=> 2
-3456	=> 18
1325132435356	=> 43

=========================================
Simple solution, mod 10 to find all digits.
    Time Complexity:    O(N)    , N = number of digits
    Space Complexity:   O(1)
'''


############
# Solution #
############

def digit_sum(number):
    x = abs(number)

    res = 0
    while x > 0:
        res += x % 10
        x //= 10

    return res

###########
# Testing #
###########

# Test 1
# Correct result => 1
print(digit_sum(10))

# Test 2
# Correct result => 2
print(digit_sum(2))

# Test 3
# Correct result => 18
print(digit_sum(-3456))

# Test 4
# Correct result => 43
print(digit_sum(1325132435356))
