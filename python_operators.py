# Mathematical Basic Operators
num1 = 10
num2 = 20

sum = 10 + 20 # 1. sum operator
multi = num1 * num2 # 2. multiply operator
div = num2 / num1 # 3. division operator

print(sum)
print(multi)
print(div)

modulo = num2 % num1 # 4, modulo operator
print(modulo)

eight_power_three = 8 ** 3 # 5. power operator 8^3
print(eight_power_three)

# String operators
statement_1: str = "Hello"
statement_2: str = ' World'

statement_3: str = statement_1 + statement_2 # 1. String concatenation
print(statement_3)

statement_1_three_times: str = statement_1 * 3 # 2. multiplying strings
print(statement_1_three_times)

world_with_space: str = statement_2
world_without_space: str = statement_2[1:6] # 3. string capture operator -> [start_with_index:end_with_index]
world_without_space_2: str = statement_2[1::] # 4. string capture operator from start_with_index to the end of string

print(world_with_space)
print(world_without_space)
print(world_without_space_2)

reverse = statement_1[::-1] # 5. reverse operator
print(reverse)

statement1_length: int = len(statement_1) # 6. len(statement1) -> lengths of statement1; len(.*) is a builtin python method
print(statement1_length)

index_of_l_character: int = statement_1.index('l') # 7. .index(.*); find index of l character in string; 'Hello' -> 2
print(index_of_l_character)

count_of_l_character: str = statement_1.count('l') # 8. .count(.*) court of character
print(count_of_l_character)
print(statement_1.count('el'))

statement_1_upper_case: str = statement_1.upper() # 9. .upper(.*) convert all letters of string to capital
print(statement_1_upper_case)

statement_1_lower_case: str = statement_1.lower() # 9. .upper(.*) convert all letters of string to small
print(statement_1_lower_case)

list_of_strs: list = "Hello mr.Basil in the course".split(" ") # 10 -> ['Hello', 'mr.Basil', 'in', 'the', 'course']
print(list_of_strs)

# List operators
"""
list is a group of items, having many indexes each index having value; such as index of 0 having 10 value
e.g:
['Hello', 50, False]
 ^        ^   ^
 |        |   |
 0        1   2

"""
_list_1: list = [10, 20, 30]
_list_2: list = [40, 50, 60]

_merge_list: list = _list_1 + _list_2 # 1. merge operator
print(_merge_list)

_list_1_three_times: list = _list_1 * 3 # 2. duplicate operator
print(_list_1_three_times)
