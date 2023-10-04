'''ar12.[adjaent]@asd.com['.'2 times not adjacent]'''
import re
while True:
    text = input("Enter the string : ")    
    #pattern = r"^a*$"   # left of string allow many times for eg: ' ', 'a','aa','aaa','aaaaaaaaa' will match
    #pattern = r"^[arun]+$"
    pattern = r"^a+$"     # left of string allow many times for eg: ___ 'a','aa','aaa','aaaaaaaaa' will match
    match = re.findall(pattern,text)
    print ("match :",match)
