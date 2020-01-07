'''
URL: https://www.hiredintech.com/classrooms/algorithm-design/lesson/23/task/32

Task: Prime counting
A classic math task is to count the prime numbers less than or equal to some integer number N. In this task you have to write a function, which does this for a given N, where 1 <= N <= 10^6. We don't count 1 a prime.

Here are a few examples:

For N=10, the prime numbers, which are less than or equal to 10 are: 2, 3, 5, 7. The function must return 4. For N=31, the prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31. The function must return 11.

=========================================
Solution: The sieve of Eratosthenes
The technique in question is called "the sieve of Eratosthenes". It allows us to find the prime numbers in a given range more quickly then just checking for each number if it's prime or not. However, it uses more memory than the previously discussed solution.

The idea is that we maintain in memory an array P, for which P[i] tells us if i is prime or not. In the beginning we set all values of P to true. Then we start to iterate from 2 up to the other end of the range to cover. For each number i we iterate we check if P[i] is currently marked as prime. If it is we run a nested loop starting from i * i with a step of i and mark the values that we iterate as not prime because obviously i is a factor for them.

The time complexity of this algorithm is known to be O(n * log log n), which is better than what we evaluated for the first solution discussed. But there is the trade-off of more memory used. The maximum memory allowed for this problem should be enough to apply this algorithm in any of the supported programming languages. But you have to be aware that at an interview you need to know what your memory constraints are. They may be very low and render this solution not suitable for the case.

Once we reach the end of the array P it will have correct values indicating, which numbers are prime. You can read a lot more about this algorithm on the Internet. There is plenty of explanation and analysis done. Here is the Wikipedia page for it.

More generally, we implemented something called a prime-counting function. There are various methods for evaluating it. You can read more about it here: prime-counting functions in Wikipedia

    Time Complexity:    O(N * log log N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

def prime_counting(n):
    is_prime = [True] * (n + 1)
    ans = 0
    print('{}: '.format(n), end='')

    for i in range(2, n+1):
        if is_prime[i]:
            print('{}, '.format(i), end='')
            ans += 1

            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return ans

###########
# Testing #
###########

# Test 1
# Correct result => 4
print('\n{}'.format(prime_counting(10)))

# Test 2
# Correct result => 11
print('\n{}'.format(prime_counting(31)))