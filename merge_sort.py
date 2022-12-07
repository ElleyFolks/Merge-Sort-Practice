def merge(num, start_index, mid_index, end_index): #function that merges two sorted partitions of number list back together

    merged_size = end_index - start_index + 1  # finding size of merged partition
    merged_numbers = [0] * merged_size # dynamically allocates temp array for merged numbers

    merge_index = 0 # position to insert merged number
    left_index = start_index # Initialized position of left partition
    right_index = mid_index +1 # Initialized position of right partition

    # first adding smallest element from left / right partitions to the merged_numbers temp array
    while (left_index <=mid_index and right_index <= end_index):
        if num [left_index] <= num[right_index]:
            merged_numbers [merge_index] = num[left_index]
            left_index+=1 # iterates through all values in left index, adding them if they are smaller

        else: #implicit logic: if above branch is false, then the value at the right index was smaller, will add this to temp array
            merged_numbers[merge_index] = num[right_index]
            right_index += 1
        merge_index+= 1

    # adds remaining elements from left partition if not empty
    while (left_index <= mid_index):
        merged_numbers[merge_index] = num[left_index]
        left_index += 1
        merge_index += 1

    #then adds remaining elements from right partition if not empty
    while (right_index <= end_index):
        merged_numbers[merge_index] = num[right_index]
        right_index += 1
        merge_index += 1

    # copy numbers from temp merge array into numbers list
    for merge_index in range(merged_size):
        num[start_index + merge_index] = merged_numbers[merge_index]


def merge_sort (numbers, first_index, last_index): #splits list of numbers into partitions to be sorted
    middle_index = 0

    if first_index < last_index:
        middle_index = (first_index + last_index)//2 #finds midpoint, where partions will be split

        #recursively sorts left (less than middle_index) and right (greater than middle_index) partitions
        merge_sort(numbers, first_index, middle_index) # left partition
        merge_sort(numbers, middle_index + 1, last_index) #right partition

        #merge left and right partitions in sorted order
        merge(numbers, first_index, middle_index, last_index)


#main program
numbers_list = [24, 0, 100, 7, 90, 43, 1, 200]
print("Initial list: ", numbers_list)

merge_sort (numbers_list, 0, len(numbers_list)-1)
print("Sorted list: ", numbers_list)