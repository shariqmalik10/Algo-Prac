'''
This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters. 
Note: a palindrome is a sequence of characters that reads the same forwards and backwards. 

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
'''
def is_plaindrome(string):
    '''
    Complexity: O(n^2)
    Removed all characters aside from alphabets and converted all to lower case
    '''
    new_str = ""
    #using negative indexing and getting the string in backwards order by assigning a negative stride (or step) value
    for i in string:
        if i.isalpha():
            new_str+=i
    return new_str.lower() == new_str.lower()[::-1]
