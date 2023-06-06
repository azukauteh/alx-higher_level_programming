#!/usr/bin/python3

# Print all the alphabet  letters
for letter in range(97, 123):
# except q and e
  if chr(letter) != 'q' and chr(letter) != 'e':
       print("{}".format(chr(letter)))
