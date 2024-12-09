"""
Conditionals:
* Conditions in python are applied by using if-statements
* Conditions idea in any programming language; is to make program decide
* If-statements flows is working by evaluating boolean values (True|False)
* pattern 1
`
if condition:
    TRUE-IF-LOGIC-1
    TRUE-IF-LOGIC-2
else:
    FALSE-IF-LOGIC-1
    FALSE-IF-LOGIC-2
    FALSE-IF-LOGIC-3
`
* pattern 2
`
if condition:
    TRUE-IF-LOGIC
elif condition:
    SECOND-TRUE-IF-LOGIC
else:
   FALSE-LOGIC
"""
_age: int = int(input("Dear user, enter your age: "))
# pattern 1
print("PATTERN #1")
if _age < 18:
    print("== Application message ==")
    print("user is defined as minor")
    print("== Application message ==")
else:
    print("== Application message ==")
    print("user is defined as adult")
    print("== Application message ==")
# pattern 2
print("PATTERN #2")
if _age < 18:
    print("== Application message ==")
    print("user is defined as minor")
    print("== Application message ==")
elif _age < 30:
    print("== Application message ==")
    print("user defining you as young")
    print("== Application message ==")
elif _age < 50:
    print("== Application message ==")
    print("user defining you as old")
    print("== Application message ==")
# pattern 3
print("pattern #3")
if _age < 18:
    print("== Application message ==")
    print("user is defined as minor")
    print("== Application message ==")
elif _age < 30:
    print("== Application message ==")
    print("user defining you as young")
    print("== Application message ==")
elif _age < 50:
    print("== Application message ==")
    print("user defining you as old")
    print("== Application message ==")
else:
    print("== Application message ==")
    print("user is not defined with this age")
    print("== Application message ==")
