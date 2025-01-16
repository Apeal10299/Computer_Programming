#When processing data it is often useful to remove the last character from some input (it is often a newline). 
#Write and test a function that takes a string parameter and returns it with the last character removed. 
#(If the string contains one or fewer characters, return it unchanged.)

def remove_last_char(s):

    if len(s) > 1:
        return s[:-1]
    return s

# Test cases
def test_remove_last_char():
    print(remove_last_char("hello"))  # Expected: "hell"
    print(remove_last_char("a"))      # Expected: "a"
    print(remove_last_char(""))       # Expected: ""
    print(remove_last_char("!"))      # Expected: "!"
    print(remove_last_char("test\n")) # Expected: "test"

test_remove_last_char()
