'''
Input: a List of integers
Returns: a List of integers
'''

new_arr = [0, 0, 0, 0, 3, 2, 1]

def moving_zeroes(arr):
    # Your code here
    new_list = []
    zero_list = []
    for i in range(len(arr)):
        if arr[i] != 0:
            new_list.append(arr[i])
        else:
            zero_list.append(arr[i])
    return new_list + zero_list

    # for i in range(len(arr)):
    #     if arr[i] == 0:
    #         arr.append(arr[i])
    #         arr.pop(i)
    # return arr

print(moving_zeroes(new_arr))

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")