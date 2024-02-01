import re 
text="new dog1233"
word=r'\bdog[0-9]*\b'
match1=re.findall(word,text)
if match1:
  print("match found")
  for a in match1:
    print(a)
