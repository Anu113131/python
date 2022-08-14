myStr = "abcdefghijklmnopqrstuvwxyzaaab"
# Slicing
print(myStr[2:6])
print(myStr[1:9])
print(myStr[1:9:3])

# String Functions
print(len(myStr))
print(myStr.endswith("xyz"))
print(myStr.startswith("abcd"))
print(myStr.count('ab'))

myStr = "my name is Anu name"
print(myStr.capitalize())
print(myStr.find("name"))
print(myStr.replace("name", "date"))