"""Count words in file."""


import sys

def word_count(file):
  opened_file = open(file)
  letter_count = {}

  for line in opened_file:
      line = line.rstrip()
      word = line.split(" ")
      for i in word:

        letter_count[i] = letter_count.get(i, 0) + 1


  for word, count in letter_count.items():
      print(f"{word} {count}")

print(word_count(sys.argv[1]))

    

# def count_char(str):
#   letter_count = {}

#   for i in str:
#     letter_count[i] = letter_count.get(i, 0) + 1

#   return letter_count