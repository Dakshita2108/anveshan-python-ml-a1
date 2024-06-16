str1 = input("Enter first string: ")
str2 = input("Enter secong string: ")
str1_lower = str1.lower()
str2_lower = str2.lower()
if(len(str1_lower) == len(str2_lower)):
      sorted_str1 = sorted(str1_lower)
      sorted_str2 = sorted(str2_lower)
      if(sorted_str1 == sorted_str2):
            print(str1,"and",str2,"are anagram")
      else:
            print(str1,"and",str2,"are not anagram")

else:
      print(str1,"and",str2,"are not anagram")
