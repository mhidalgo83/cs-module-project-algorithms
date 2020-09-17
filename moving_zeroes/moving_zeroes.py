'''
Input: a List of integers
Returns: a List of integers
'''



def moving_zeroes(arr):
    # Your code here
    # First pass solution:
    # new_list = []
    # zero_list = []
    # for i in range(len(arr)):
    #     if arr[i] != 0:
    #         new_list.append(arr[i])
    #     else:
    #         zero_list.append(arr[i])
    # return new_list + zero_list

    # Refactored code, implemented in one line
    return [n for n in arr if n != 0] + [n for n in arr if n == 0]


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")