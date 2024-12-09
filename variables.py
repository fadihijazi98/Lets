"""
Defining variables & Variables data types
"""
age = 25 # integer values (int)
sale = 9.99 # real-number values (float)
isMale = True # boolean values (bool)
isFemale = False # boolean values (bool)
question = "what is your name?" # string values (str)

"""
How we could using variables in python
"""
print(age)
print(sale)
print(isMale)
print(isFemale)
print(question)

"""
Variables naming rules
"""
_variable1 = "any" # variable could not start with any character & numbers (e.g:`$`,`^`,..etc.) except underscore (`_`)

"""
Variables naming conventions:
1. Snake Case: is_basil_programmer (recommended in python to define variables & methods)
2. Pascal Case: IsBasilProgrammer
3. Camel Case: isBasilProgrammer
"""
is_basil_programmer = "Yes, I am a programmer"
print(is_basil_programmer)

"""
Python is datatype less language
"""
age = 25 # age variable starting with integer
print(age)
age = "25 years old" # age value updated to be string
print(age)
age = True # finally age value updated to be boolean
print(age)
"""
Python is support type hinting
type hinting work like -> variable_name: data_type = 
Example: age: int = 25
"""
age: int = 25
message: str = "Hello, World!"
flag: bool = True
