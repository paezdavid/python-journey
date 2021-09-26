
# First version of the program. This approach is too verbose and with many unnecessary code.

# def reverseString(stringToReverse):
#     initialArr = []
#     reversedArr = []

#     if type(stringToReverse) == str:
#         for i in range(len(stringToReverse)):
#             initialArr.append(stringToReverse[i])

#         for item in initialArr:
#             reversedArr.insert(0, item)
        
#         reversedString = ''.join(reversedArr)

#         return reversedString
#     else:
#         return TypeError("Error: Argument passed to function should be a string")

# print(reverseString(1)) # error
# print(reverseString("hello")) # olleh



#########################################################################################################
# Second version (Code improved. Turns out I can just iterate directly over the string passed as an argument instead of creating a new array!)


# def reverseString(stringToReverse):
#     reversedArr = []

#     if type(stringToReverse) == str:
#         for item in stringToReverse:
#             reversedArr.insert(0, item)
        
#         reversedString = ''.join(reversedArr)

#         return reversedString
#     else:
#         return TypeError("Error: Argument passed to function should be a string")

# print(reverseString(1)) # error
# print(reverseString("hello")) # olleh
# print(reverseString("alo")) # ola

#########################################################################################################

# Third version. With a bit of modification I could make it so that my function reverse either a list or a string.

# def reverseListOrStr(dataToReverse):
#     reversedList = []
    
#     if type(dataToReverse) == str or type(dataToReverse) == list:
#         for item in dataToReverse:
#             reversedList.insert(0, item)

#     if type(dataToReverse) == str:
#         reversedString = ''.join(reversedList)
#         return reversedString
#     elif type(dataToReverse) == list:
#         return reversedList
#     else:
#         return TypeError("Error: Argument passed to function should be a string or a list")

# print(reverseListOrStr("hello")) # olleh
# print(reverseListOrStr([1, 2, 3])) # [3, 2, 1]
# print(reverseListOrStr(123)) # ???


#########################################################################################################
# Fourth version. Used slicing to reverse the data passed as an argument! (now tuple included)

def reverseData(dataToReverse):
    reversedList = []
    
    if (type(dataToReverse) == str or
        type(dataToReverse) == list or
        type(dataToReverse) == tuple):

        reversedList = dataToReverse[::-1]
    else:
        return TypeError("Error: Data passed should be a string, a list or a tuple")

    return reversedList


print(reverseData([1, 2, 3])) # [3, 2, 1]
print(reverseData("nice")) # ecin
print(reverseData((1, "hi", 2))) # (2, "hi", 1)
print(reverseData(123)) # error!

