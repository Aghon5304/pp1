import re
text= "To be, or not to be, that is the question"
samogloski = re.findall("[aeiouy]",text)
samogloski = len(samogloski)
print(f"jest {samogloski} samoglosek!")