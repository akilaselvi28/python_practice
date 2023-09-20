# Sample array
array = [12, 45, 6, 78, 34, 90, 56, 89, 23]

# 1. Find the mid value of the array
mid_value = array[len(array) // 2]
print("The mid value of array is: ",mid_value)
# 2. Find max and min value from the array
max_value = max(array)
min_value = min(array)
print("The max & min value of given array are : " ,max_value,min_value)
# 3. Find 2nd max and 2nd min value from the array
sorted_array = sorted(array)
second_max = sorted_array[-2]
second_min = sorted_array[1]
print("The second min & max values are : " ,second_max,second_min)
# 4. Sum the array's values
array_sum = sum(array)
print("Total: ",array_sum)
# 5. Print only odd index values
odd_index_values = [array[i] for i in range(1, len(array), 2)]
print("The odd index values: ",odd_index_values)
# 6. Print only even index values
even_index_values = [array[i] for i in range(0, len(array), 2)]
print("The even index value : " ,even_index_values)
# 7. Sort the array in ascending order (without using predefined functions)
def custom_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

ascending_sorted_array = custom_sort(array.copy())
print("The ascending sorted array : ", ascending_sorted_array)
# Sort the array in descending order (without using predefined functions)
def custom_sort_desc(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

descending_sorted_array = custom_sort_desc(array.copy())
print("The descending sorted array : ",descending_sorted_array)
# 8. Find the weightage of the first half or second half
half = len(array) // 2
sum_first_half = sum(array[:half])
sum_second_half = sum(array[half:])
print("The sum first & second half is :", sum_first_half , sum_second_half)
# 9. Print only prime numbers from the array
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in array if is_prime(num)]
print("The prime numbers : ",prime_numbers)
# 10. Print the index of the value 40 or indicate if not found
search_value = 40
index = -1  # Default value if not found
for i in range(len(array)):
    if array[i] == search_value:
        index = i
        break

if index == -1:
    print(f"There is no such value {search_value} in the array.")
else:
    print(f"The value {search_value} is found at index {index}.")