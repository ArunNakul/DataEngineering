import re

while True:

    text = input(" Enter the String : ")
    pattern = r"\S" # match all non-whitespace characters for eg: "arun"           #All three are same
    pattern = r"[^ \n\r\t\f]" # match all non-whitespace characters for eg: "arun" #All three are same
    pattern = r"[^\s]" # match all non-whitespace characters for eg: "arun"        #All three are same
    file1 = open("myfile.txt","r+")

    text1 = file1.read()

    match = re.findall(pattern,text1)

    print("match : ",match)