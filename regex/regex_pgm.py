import re
text = " hello Ajay"
pattern = r"\d"
match = re.match(pattern, text)
print ("match :",match)