# def my_function():
#   print("Hello from a function")

# my_function()




# def get_greeting():
#   return "Hello from a function"

# message = get_greeting()
# print(message)


# def my_function(name): # name is a parameter
#   print("Hello", name)

# my_function("Emil") # "Emil" is an argument



# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(name = "Buddy", animal = "dog")



# def my_function(person):
#   print("Name:", person["name"])
#   print("Age:", person["age"])

# my_person = {"name": "Emil", "age": 25}
# my_function(my_person)



# def my_function(*, name):
#   print("Hello", name)

# my_function(name = "Emil")



# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")



# def my_function(*args):
#   print("Type:", type(args))
#   print("First argument:", args[0])
#   print("Second argument:", args[1])
#   print("All arguments:", args)

# my_function("Emil", "Tobias", "Linus")




# def my_function(greeting, *names):
#   for name in names:
#     print(greeting, name)

# my_function("Hello", "Emil", "Tobias", "Linus")




# def my_function(*numbers):
#   if len(numbers) == 0:
#     return None
#   max_num = numbers[0]
#   for num in numbers:
#     if num > max_num:
#       max_num = num
#   return max_num

# print(my_function(3, 7, 2, 9, 1))


# def my_function(fname, lname):
#   print("Hello", fname, lname)

# person = {"fname": "Emil", "lname": "Refsnes"}
# my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")




x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)




