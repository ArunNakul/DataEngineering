input_string = 'heart'
compare_string = 'earth'
char_dict = {}
char_dict1 = {}
for char in input_string:
    print("char = ",char)
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1
print ("first dictionary : ", char_dict)
for char in compare_string:
    print("char = ",char)
    if char in char_dict1:
        char_dict1[char] += 1
    else:
        char_dict1[char] = 1
print ("compare dictionary : ", char_dict1)
if char_dict == char_dict1:
    print(" This is Anagram")
else:
    print("This is not a Anagram")
# step 1 = read a and assign to dictionary {h:1,e:1,a:1,r:1,t:1}

# step 2 = read b and assing to another dictionary {e:1,a:1,r:1,t:1,h:2}
# step 3 = for ( get the dictionary elements one by one) and compare with second dictionary
# step 4 = if both the elements are not match then break the loop
# step 5 = if flag_anagram is false then print it is not anagram
# step 6 = else  print it is anagram






