'''
Write a Python function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
Requirements:
The function should count both lowercase and uppercase vowels.
It should return an integer representing the total number of vowels in the string.
Consider edge cases like an empty string or a string with no vowels.
'''

def count_vowels(text):
    vowels = 'aeiou'
    vowels = list(vowels) + list(vowels.upper())
    print(vowels)

    if not text:
        print('Please enter a valid text')
        return 

    count = 0
    for i in text:
       if i in vowels:
           print(i)
           count = count + 1 
    if count == 0:
        print('you have no vowels in text.')
    else:
        print(f'You have {count} vowels in your string.')



text = input('enter text')
count_vowels(text)


#after verifying scope of improvements 

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    
    if not text:
        print('Please enter a valid text')
        return 

    count = 0
    for i in text:
       if i in vowels:
           count += 1
    
    if count == 0:
        print('You have no vowels in your text.')
    else:
        print(f'You have {count} vowels in your string.')

# Example usage
text = input('Enter text: ')
count_vowels(text)

#proffesional_approch

def count_vowels(text):
    # Define a set of vowels for quick lookup
    vowels = set('aeiouAEIOU')
    
    # Check for empty input
    if not text:
        raise ValueError('Input text cannot be empty')
    
    # Count vowels using a generator expression
    count = sum(1 for char in text if char in vowels)
    
    # Return the result
    return count

# Example usage
try:
    text = input('Enter text: ')
    vowel_count = count_vowels(text)
    if vowel_count == 0:
        print('You have no vowels in your text.')
    else:
        print(f'You have {vowel_count} vowels in your string.')
except ValueError as e:
    print(e)

