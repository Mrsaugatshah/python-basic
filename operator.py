# x = 15
# y = 4

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x ** y)
# print(x // y)


# numbers = [1, 2, 3, 4, 5]
# count = len(numbers)
# if count > 3:
#     print(f"List has {count} elements")

# if (count := len(numbers)) > 3:
#     print(f"List has {count} elements")


# x = 5
# y = 3

# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)


# x = 5

# print(not(x > 3 and x < 10))


# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# print(x is y)
# print(x == y)



# text = "Hello World"

# print("H" in text)
# print("hello" in text)
# print("z" not in text)



# Title: Check Even or Odd using Bitwise Operators
# Objective: Determine if a number is even or odd using bitwise operations
# Remarks: Bitwise AND with 1 isolates the least significant bit

# def is_even(number):
#     return (number & 1) == 0

# # Test the function
# numbers = [10, 15, 22, 33, 42]

# for num in numbers:
#     if is_even(num):
#         print(f"{num} is Even")
#     else:
#         print(f"{num} is Odd")




a = 5
b = 2
c = 8

result = a + b << 2 & c
print(result)
