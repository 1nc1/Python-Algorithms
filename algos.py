# Create a function that, given an input string str , returns a boolean whether
# parentheses in str are valid. Valid sets of parentheses always open before
# they close, for example. For "Y(3(p)p(3)r)s" , return true . Given "N(0(p)3" ,
# return false : not every parenthesis is closed. Given "N(0)t ) 0(k" , return
# false , because the underlined ")" is premature: there is nothing open for it
# to close.

# def parensValid(str):
#     parenString = ''
#     count = 0
#     for i in range(len(str)):
#         if str[i] == '(':
#             parenString += str[i]
#             count += 1
#         if str[i] == ')':
#             parenString += str[i]
#             count -= 1
#         if count < 0:
#             return False
#     if count == 0:
#         return True
#     else:
#         return False
    

# print(parensValid('Y(n) (63 ( 7) v())'))

# ------------------------------------------------------
# Create a function that returns a boolean whether the string is a strict
# palindrome. For "a x a" or "racecar" , return true . Do not ignore spaces,
# punctuation and capitalization: if given "Dud" or "oho!" , return false .

# Second: now do ignore white space (spaces, tabs, returns), capitalization and
# punctuation.

# def isPalindrome(str):
#     revStr = str[::-1].split()
#     str = str.split()
#     str = ''.join(str).upper()
#     revStr = ''.join(revStr).upper()
#     if revStr == str:
#         return True
#     else:
#         return False

# print(isPalindrome('r       aceca   yr'))
