import re

while True:

    text = input("Enter the string : ")

    pattern = r"\b"  #DOUBT

    file1 = open("myfileA.txt","r+")

    text1 = file1.read()

    match = re.findall(pattern,text1)

    print ("match : ",match)

    """
    Matches the empty string, but only at the beginning or end of a word. 
    A word is defined as a sequence of word characters. 
    Note that formally, \b is defined as the boundary between a \w and a \W character (or vice versa), 
    or between \w and the beginning/end of the string. 
    This means that r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
    """