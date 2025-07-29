#Data Types using snake_case naming
student_name = "Karen Wanjiru" # String
print(student_name) # Output: Karen Wanjiru

student_ID = 12345 # Integer
print(student_ID) # Output: 12345

student_age = 10 #Integer
print(student_age) # Output: 10

student_height = 1.45 # Float
print(student_height) # Output: 1.45

fees_clearance = True # Boolean
print(fees_clearance) # Output: True

languages = ["Python", "Java", "JavaScript"] # List
print(languages) # Output: ['Python', 'Java', 'JavaScript']

student_subjects = ("Math", "Science", "English") # Tuple
print(student_subjects) # Output: ('Math', 'Science', 'English')

student_address = {"city": "Nairobi", "country": "Kenya"} # Dictionary
print(student_address) # Output: {'city': 'Nairobi', 'country': 'Kenya'}

student_ids = {112, 114, 117, 113} # Set
print(student_ids) # Output: {112, 113, 114, 117}

#printing on one line
print(student_name, student_ID, student_age, fees_clearance)

# Accessing elements in a list
print(languages[0]) # Output: Python, the first element in the list
# Accessing elements in a tuple
print(student_subjects[1]) # Output: Science, the second element in the tuple
# Accessing values in a dictionary
print(student_address["city"]) # Output: Nairobi, the value associated with the key "city"
# Accessing elements in a set
''' Note: Sets are unordered, so we cannot access elements by index.
However, we can check for membership '''
print(112 in student_ids) # Output: True, checks if 112 is in the set of student_ids

# Arithmetic operations
add = 5 + 2 # Addition
print(add) # Output: 7
subtract = 5 - 2 # Subtraction
print(subtract) # Output: 3
multiply = 5 * 2 # Multiplication
print(multiply) # Output: 10
divide = 5 / 2 # Division
print(divide) # Output: 2.5
modulus = 5 % 2 # Modulus
print(modulus) # Output: 1, remainder of the division
exponent = 5 ** 2 # Exponentiation
print(exponent) # Output: 25, 5 raised to the power of 2
floor_divide = 5 // 2 # Floor Division
print(floor_divide) # Output: 2, division without the decimal part

# Comparison operations. They return True or False
is_equal = (5 == 5) # Equal to
is_not_equal = (5 != 2) # Not equal to
is_greater = (5 > 2) # Greater than
is_less = (5 < 2) # Less than
is_greater_or_equal = (5 >= 5) # Greater than or equal to
is_less_or_equal = (5 <= 2) # Less than or equal to

# Logical operations. They return True or False
and_operation = (5 > 2) and (3 < 5) # Logical AND
print(and_operation) # Output: True, both conditions are true
or_operation = (5 > 2) or (3 > 5) # Logical OR
print(or_operation) # Output: True, at least one condition is true
not_operation = not (5 > 2) # Logical NOT
print(not_operation) # Output: False, negates the condition

# Another example of logical operations
a = 10
b = 20
c = 30
print(a < b and b < c) # Output: True
print(a < b or b > c) # Output: True
print(not (a < b)) # Output: False




