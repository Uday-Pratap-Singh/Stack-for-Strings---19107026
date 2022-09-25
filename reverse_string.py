
def createStack():
    stack = []
    return stack
 

def size(stack):
    return len(stack)
 

def isEmpty(stack):
    if size(stack) == 0:
        return True
 
 
def push(stack, item):
    stack.append(item)


def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()

 
def reverse(string):
    n = len(string)
 
    stack = createStack()
 
    # Push all the characters of the string to the stack
    for i in range(0, n):
        push(stack, string[i])
 
    """Making the string empty since all
       characters are saved in the stack"""
    string = ""
 
    """ Pop all characters of the string and
        put them back in the string"""
    for i in range(0, n):
        string += pop(stack)
 
    return string
 
 
# main program 
string = input()
string = reverse(string)
print("Reversed string is " + string)
