'''
Lab 22 - Practice Problems
Problem 3: Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
'''


def find_pair(nums, target):  # define find_pair function

    chkd_nums = []  # define list of checked numbers, prevents duplicate sets
    pair_nums = []  # define list of pairs that sum to target

    for num in nums:  # run through list of numbers
        diff = target - num  # subtract number from target sum, assign to variable for difference
        if diff in chkd_nums:  # if the difference is in the list of check numbers, return number and difference number
            pair_nums.append([num, diff])
        else:
            chkd_nums.append(num)  # add number to checked number list
    return pair_nums  # return list of pairs that sum to target


nums_list = [4, 6, 2, 3, 5, 1]  # define number list

target_num = 7  # define target number

print(find_pair(nums_list, target_num))  # pass arguments to function and print result
