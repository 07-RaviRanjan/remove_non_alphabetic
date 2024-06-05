def remove_non_alphabetic(text):
  return ''.join(char for char in text if char.isalpha())

text = "This is a string with characters like #, $ and %."
result = remove_non_alphabetic(text)
print(result)
