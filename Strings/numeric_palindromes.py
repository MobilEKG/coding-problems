'''
URL: https://www.hiredintech.com/classrooms/algorithm-design/lesson/76/task/29

Task: Numeric Palindromes
A palindrome is а word or a phrase or a number, that when reversed, stays the same.
For example, the following sequences are palindromes : "azobi4amma4iboza" or "anna".
But this time, we are not interested in words but numbers. A "number palindrome" is a number, that taken backwards, remains the same.
For example, the numbers 1, 4224, 9999, 1221 are number palindromes.
Implement a function, which given an integer computes if it's a palindrome.

Input: One integer n, where 0 < n <= 10,000,000,000.

Output: Your function must return a boolean true if n is a palindrome and false otherwise.

Test examples
1	=> true
42	=> false
100001	=> true
999	=> true
123	=> false

=========================================
Simple algorithm, for each position compare left and right side of the input.
    Time Complexity:    O(N)
    Space Complexity:   O(1)

'''


############
# Solution #
############

def is_numeric_palindrome(n):
    result = True

    str_n = str(n)
    len_n = len(str_n)

    for i in range(len_n//2):
        if (str_n[i] != str_n[len_n - 1 - i]):
            result = False
            break

    return result

###########
# Testing #
###########

# Test 1
# Correct result => True
print(is_numeric_palindrome(1))

# Test 2
# Correct result => Flase
print(is_numeric_palindrome(42))

# Test 3
# Correct result => True
print(is_numeric_palindrome(100001))

# Test 4
# Correct result => True
print(is_numeric_palindrome(999))

# Test 5
# Correct result => Flase
print(is_numeric_palindrome(123))


