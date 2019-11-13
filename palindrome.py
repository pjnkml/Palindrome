def IsPalindrome(str):
    """This function check whether the word is a palindrom"""
    if str == str[::-1]:
        return True
    else:
        return False

str = "malayalam"
print("It is {} that {} is a palindrome".format(IsPalindrome(str),str))
