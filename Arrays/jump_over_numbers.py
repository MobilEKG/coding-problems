'''
URL: https://www.hiredintech.com/classrooms/algorithm-design/lesson/76/task/26

You are given a list of non-negative integers and you start at the left-most integer in this list. After that you need to perform the following step:
Given that the number at the position where you are now is P you need to jump P positions to the right in the list. For example, if you are at position 6 and the number at position 6 has the value 3, you need to jump to position 6 + 3 = 9. Repeat this operation until you reach beyond the right-side border of the list.
Your program must return the number of jumps that it needs to perform following this logic. Note that the list may contain the number 0, which mean that you can get stuck at a this position forever. In such cases you must return the number -1.

The length N of the input list will be in the range [1, 1000].

SAMPLE INPUT: 3 4 1 2 5 6 9 0 1 2 3 1
SAMPLE OUTPUT: 4

Note: In the sample example you start at position 1, where the number is 3. Then you must jump to position 4, where the number is 2. After that you jump to position 6 where the number is 6. This will lead you to position 12, which is the last number in the list and has the value 1. From there you jump 1 position to the right and must stop. This is a total of 4 jumps.

=========================================
Solution 1:
Computer the first jump distance, then iterate the array:
- if current index less than (jump distance - 1), continue iteration;
- otherwise if current value equals to 0, returns -1;
- otherwise recalculate jump distance and increase jump counter by one;

    Time Complexity:    O(N)
    Space Complexity:   O(1)

Solution 2

    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


##############
# Solution 1 #
##############
def jump_over_numbers1(list):
    if list[0] == 0:
        print('{} at pos {}'.format(list[0], 1))
        return -1

    result = 1
    jump = list[0] + 1
    print('{} at pos {} jumps to {}'.format(list[0], 1, jump))

    for i in range(len(list)):
        if i == jump - 1:
            if list[i] == 0:
                print('{} at pos {}'.format(list[i], i + 1))
                result = -1
                break
            else:
                jump = list[i] + (i + 1)
                result += 1
                print('{} at pos {} jumps to {}'.format(list[i], i + 1, jump))

    return result

##############
# Solution 2 #
##############
def jump_over_numbers2(list):
    pos = 0
    ans = 0
    while pos < len(list):
        if list[pos] == 0:
            print('{} at pos {}'.format(list[pos], pos + 1))
            return -1

        print('{} at pos {} jumps to {}'.format(list[pos], pos + 1, pos + 1 + list[pos]))
        ans += 1
        pos += list[pos]

    return ans

###########
# Testing #
###########

# Test 1
# Correct result: 4
print(jump_over_numbers1([3, 4, 1, 2, 5, 6, 9, 0, 1, 2, 3, 1]))
print(jump_over_numbers2([3, 4, 1, 2, 5, 6, 9, 0, 1, 2, 3, 1]))

# Test 2
# Correct result: -1
print(jump_over_numbers1([3, 4, 1, 4, 5, 6, 9, 0, 1, 2, 3, 1]))
print(jump_over_numbers2([3, 4, 1, 4, 5, 6, 9, 0, 1, 2, 3, 1]))

# Test 3
# Correct result: -1
print(jump_over_numbers1([0, 4, 1, 4, 5, 6, 9, 0, 1, 2, 3, 1]))
print(jump_over_numbers2([0, 4, 1, 4, 5, 6, 9, 0, 1, 2, 3, 1]))