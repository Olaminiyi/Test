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

