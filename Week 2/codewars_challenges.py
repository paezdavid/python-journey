# 1 - Create a function that takes a list of non-negative integers and strings 
# and return a new list with the strings filtered out.

def filter_list(listt):
    filteredList = []
    for item in listt:
        if type(item) != str:
            filteredList.append(item)
    return filteredList


print(filter_list([1, "a", 2, 3, "a", "Goku", 8, "b"])) # [1, 2, 3, 8]


# 2 - Create a function that returns the sum of the two lowest positive numbers 
# given an array of minimum 4 positive integers.
# No floats or non-positive integers will be passed.

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
    
print(sum_two_smallest_numbers([5, 19, 2, 3, 1, 21])) # 3