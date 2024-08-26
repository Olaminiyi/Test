import re

text_to_search = '''
abc defghij klmnoprs tucxyz abcd eabc
awwff gghhjj ac
'''
sentence = 'abc defgh ijkl baba ca'
pattern = re.compile(r'^ab')
matches = pattern.finditer(sentence)

for match in matches:
   # print(f"found '{match.group()}' at positon {match.start()}-{match.end()}")
    print(match)
#print(text_to_search[1:4])

# -------------------------------------
# .  - Any character Except New license
# \d - Digit (0-9)
# \D - Not a Digit (0-9)
# \w - word character (a-z, A-Z, 0-9, _)
# \W - Not a Word Character
# \s - Whitespace (space, tab, newline)
# \S - Not Whitespace (space, tab, newline)

# \b - Word Boundaary
# \B - Not a Word Boundary
# ^  - Beginning of a String 
# $  - End of a String 

# [] - Matches Characters in brackets 
# [^] - Matches Character NOT in brackets
