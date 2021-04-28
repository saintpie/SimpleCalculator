first_num = float(input())
second_num = float(input())
action = input()
operations = {"mod": "%", "div": "//", "pow": "**"}
try:
    print(eval("(" + str(first_num) + ")" + operations.get(action, action) + str(second_num)))
except ZeroDivisionError:
    print("Деление на 0!")