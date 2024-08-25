import re

text_to_search = '''
abcdefghijklmnoprstucxyzabcdeabc

'''

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(f"found '{match.group()}' at positon {match.start()}-{match.end()}")

print(text_to_search[1:4])