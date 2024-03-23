import re

text = """
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'
"""
pattern = r'Alice'

match = re.match(pattern, text)
if match:
    print("Match found at the beginning of the text:", match.group())
else:
    print("No match found at the beginning of the text.")

search = re.search(pattern, text)
if search:
    print("Pattern found anywhere in the text at index:", search.start())
else:
    print("Pattern not found anywhere in the text.")

findall = re.findall(pattern, text)
if findall:
    print("All occurrences of the pattern in the text:", findall)
else:
    print("No occurrences of the pattern found in the text.")
