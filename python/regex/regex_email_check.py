import re

while True:

    text = input("Enter the String : ")

    #pattern = r"[a-z0-9\_][@][a-z][.]{1,2}[.com|.co.in]"
    #pattern = r"(.com|.co.in)\.{1,2}"
    pattern = r"([a-z0-9].+\@[a-z]+\.(com)$)"
    match = re.findall(pattern,text)

    print ("match : ",match)
