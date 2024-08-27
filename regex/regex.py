import re

# text_to_search = '''
# abc defghij klmnoprs tucxyz abcd eabc
# awwff gghhjj ac
# '''
# sentence = 'abc defgh ijkl baba ca'
# pattern = re.compile(r'^ab')
# matches = pattern.finditer(sentence)

# for match in matches:
#    # print(f"found '{match.group()}' at positon {match.start()}-{match.end()}")
#     print(match)
# #print(text_to_search[1:4])

pattern = re.compile(r'\d{3}.*\w+.*[a-zA-Z]\.,.*[a-zA-Z].*[A-Z].*\d{5}')

with open('data.txt','r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)



#245 Washington St., Bedrock IL 26941