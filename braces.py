def braces(s):
    BRACES = { '(': ')', '[': ']', '{': '}' }
    stack = []
    for b in s:
        c = BRACES.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack


def palindrome(word):
    if word == word[::-1]:
        return True

def main():
    while True:
        task = input("Check the parentheses: press '1'\nCheck if palindrome: press '2'\nQuit: press 'q'\n")
        if task == '1':
            braces_input = input("Enter braces: \nValid braces: {}()[]\n")
            if braces(braces_input):
                print("Valid braces")
            else:
                print("Invalid braces")
        elif task == '2':
            word = input("Enter a string: ")
            if palindrome(word):
                print("Its a palindrome")
            else:
                print("Not a palindrome")
        elif task == 'q':
            break

main()
