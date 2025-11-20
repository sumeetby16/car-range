import sys

if len(sys.argv) != 5:
    print("Usage: python student.py <name> <roll>")
    sys.exit(1)

script_name = sys.argv[0]
name = sys.argv[1]
id = sys.argv[2]
sal = sys.argv[3]
exp = sys.argv[4]



print("Script Name:", script_name)
print("Employee Name:", name)
print("Employee ID:", id)
print("Employee Salary:", sal)
print("Employee Experience:", exp)