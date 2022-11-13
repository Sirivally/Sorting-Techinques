from random import randint
def lomuto_sort(nums, low, high):
    if low >= high:
        return

    pivotIdx = randint(low, high)
    nums[pivotIdx], nums[high] = nums[high], nums[pivotIdx]
    i, pivot = low, nums[high]

    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = pivot, nums[i]

    lomuto_sort(nums, low, i - 1)
    lomuto_sort(nums, i + 1, high)
          
lomuto_sort(nums,0,len(nums)-1)