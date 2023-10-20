import re

while True:
    text = input ("Enter the string: ")
    #pattern = r"^a..$"   #starts with 'a' character and any 2 charachers will match in this expression
    #pattern = r"a.."   #split the string with starts a character in multiple sets
    #pattern = r"a..$"   #strings with a with 2 characters
    #pattern = r"^a\?$"  # check the string has 'a?'
    #pattern = r"Arun|Ajay"  # check the strings any occurence in the string with Arun or Ajay
    pattern = r"^Arun|Ajay$" # check the strings starts with 'Arun' and end with 'Ajay'
    match = re.findall(pattern,text)
    print("match : ",match)
    print("count : ",len(match))
