'''
Write a Python function that takes a string as input and checks if it is a palindrome.
A palindrome is a word, phrase, or sequence of characters that reads the same forward 
and backward (ignoring spaces, punctuation, and case).
'''

def is_palindrome(text):

    txt = text.lower().replace(' ','').replace(',','')
    A = txt[::-1]
    
    if A == txt:
        print('the text is palindrome')
    else:
        print('not a palindrome')

text = input('enter text here :')
is_palindrome(text)




#suggested code improved 

import re

def is_palindrome(text):
    # Normalize the text: convert to lowercase and remove non-alphanumeric characters
    normalized_text = re.sub(r'[^a-z0-9]', '', text.lower())
    
    # Check if the normalized text is the same forwards and backwards
    if normalized_text == normalized_text[::-1]:
        return True
    else:
        return False

# Example usage
text = input('Enter text here: ')
if is_palindrome(text):
    print('The text is a palindrome.')
else:
    print('Not a palindrome.')
