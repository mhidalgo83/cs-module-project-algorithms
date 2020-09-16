'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

'''
# arr = [70, 37, 100, 66, 1, 45, 27, 62, 75, 57, 92, 66, 9, 39, 15, 69, 46, 72]

def sliding_window_max(nums, k):
    max_list = []
    start = 0
    end = k
    count = 0
    max_val = min(nums)
    while count < (len(nums) - k + 1):
        for i in nums[start:end]:
            if max_val < i:
                max_val = i
        max_list.append(max_val)
        start += 1
        end += 1
        count +=1
        max_val = min(nums)
    return max_list




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    # arr = [1, 3, -1, -3, 5, 3, 6, 7]
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
