s = "0123456789"
print(s)
print(s[1:2])  # First index is included, last index is excluded
print(s[1:7])  #see now it excludes the last one (7) and puts 1-6.
print(s[:7]) # you omit with the : as you can see in all examples, if u omit the first index, it starts from the beginning.

s = "I go to school early in the am's"
print(s[20:]) #now it cut out the first 20 letters and spaces and left what's remaining.

print(s[:]) #includes the whole message written in s.
print(s[::2]) #it prints every second character.
