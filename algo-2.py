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
    Complexity: 
    '''
    #using negative indexing and getting the string in backwards order by assigning a negative stride (or step) value 
    return string == string[::-1]
