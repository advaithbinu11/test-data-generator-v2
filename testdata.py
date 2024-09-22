import random
import pprint
def generate_test(binput):
    converter = {"\\d": "[0-9]", "\\D": "[^0-9]", "\\w": "[a-zA-Z0-9_]", "\\W": "[^a-zA-Z0-9_]"}
    lastpattern = ""
    result = ""
    uinput=binput
    # Convert backslash shortcuts
    while "\\" in uinput:
        ind = uinput.find("\\")
        reg = uinput[ind:ind + 2]
        uinput = uinput[:ind] + converter.get(reg, reg) + uinput[ind + 2:]

    # Process regex expression
    while uinput != "":
        if uinput[0] == "[":
            lastpattern = uinput[1:uinput.find("]")]
            uinput = uinput[uinput.find("]") + 1:]
            result += squared(lastpattern)
        elif uinput[0] == "{":
            t = uinput.find("}")
            times_to_repeat = times(uinput[1:t])
            for i in range(times_to_repeat-1):
                result += squared(lastpattern)
            uinput = uinput[t + 1:]  # Move past the closing curly brace
        else:
            result += uinput[0]
            uinput = uinput[1:]
    return result
def times(expression):
    comma = expression.find(",")
    if comma != -1:
        first = int(expression[0:comma])
        second = int(expression[comma + 1:])
        return random.randrange(first, second+1)
    return int(expression)

def squared(expression):
    dash = expression.find("-")
    while dash != -1 and dash>0 and dash<len(expression)-1:
        first = ord(expression[dash - 1])
        second = ord(expression[dash + 1])
        save1=expression[:dash - 1]
        save2=expression[dash + 2:]
        expression=""
        for i in range(first, second + 1):  # Include second value
            expression += chr(i)
        expression = save1+expression+save2
        dash = expression.find("-")
    return expression[random.randrange(0, len(expression))]


if __name__ == "__main__":

    # Check for empty strings or string with only spaces
    # This step is not required here
    # if not bool(city.strip()):
    #     city = "Kansas City"
    print("How many test cases?")
    testcases = int(input())
    print("Type a regex expression:")
    binput = input()
    result = []
    for i in range(testcases):
        result.append(generate_test(binput))

    print("\n")
    pprint.pprint(result)
