# Codewar: Mumbling
# transfer the string in-place in the original string, O(n) time complexity and O(1) extra space complexity
def accum(s):
    # if the input is None or 0 length, it will not work for the while loop
    if s == None or len(s) == 0:
        return s

    # because python string is immutable, so we need to tranfer the string to a character list
    s_list = list(s)

    # length of the string, it will also record how many char we need to duplicate
    n = len(s)

    # this problem asks for extra space, the variable will record the length of the extra space
    # it's -1, because we need (n-1)'s '-', but the original char list's length is n
    extra_space = -1

    # we need one s[0], two s[1], three s[2], and etc.
    for i in range(1, n + 1):
        extra_space += i

    # assign ' ' to the extra space
    for i in range(extra_space):
        s_list.append(' ')

    # left pointer will start at the last char in the original string
    left = n - 1

    # right pointer will start at the last index in the output string
    right = n + extra_space - 1

    # while left is not the 1st char, we will continue to replace the current space or character to valid characters 
    while left > 0:
        # make sure the char will be lowwer case
        temp = s_list[left].lower()

        # replace the current index with the lower case char, the length will be n - 1, because the first char will be upper case
        for i in range(n - 1):
            s_list[right] = temp
            right -= 1
        
        # upper case the first char
        s_list[right] = temp.upper()
        right -= 1

        # add '-' before the 1st char
        s_list[right] = '-'
        right -= 1
        
        # length will be minus 1, to record how many char we need to replace in the character list
        n -= 1
        left -= 1

    # we change the 1st char to upper case character
    s_list[left] = s_list[left].upper()
    
    # return a string
    return ''.join(s_list)

# some test cases
print(None)
print('')
print('a')
print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))
print(accum('None'))