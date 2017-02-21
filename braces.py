def braces(s):
    BRACES = { '(': ')', '[': ']', '{': '}' }
    stack = []
    for b in s:
        for i in b:
            c = BRACES.get(b)
            if c:
                stack.append(c)
            elif not stack or stack.pop() != b:
                return False
    return not stack

braces_input = input("Enter braces: \nValid braces: {}()[]\n")
if braces(braces_input):
    print("Valid")
else:
    print("Invalid")
