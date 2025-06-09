def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

# Example usage
word = "A man, a plan, a canal: Panama"
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
